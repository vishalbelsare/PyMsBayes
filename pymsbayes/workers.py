#! /usr/bin/env python

import os
import sys
import re
import subprocess
import time
import shutil
import traceback
from cStringIO import StringIO

from pymsbayes.utils.tempfs import TempFileSystem
from pymsbayes.utils import BIN_DIR
from pymsbayes.utils.functions import (get_random_int, expand_path,
        get_indices_of_patterns, reduce_columns, process_file_arg)
from pymsbayes.utils.errors import WorkerExecutionError
from pymsbayes.utils.messaging import get_logger

_LOG = get_logger(__name__)


##############################################################################
## msBayes prior header patterns

PARAMETER_PATTERNS = [
        re.compile(r'\s*PRI\.(?!numTauClass)\S+\s*$'),
        ]
DEFAULT_STAT_PATTERNS = [
        re.compile(r'\s*pi\.\d+\s*'),
        re.compile(r'\s*wattTheta\.\d+\s*'),
        re.compile(r'\s*pi\.net\.\d+\s*'),
        re.compile(r'\s*tajD\.denom\.\d+\s*'),
        ]
ALL_STAT_PATTERNS = [
        re.compile(r'\s*(?!PRI)\S+\s*$'),
        ]
DUMMY_PATTERNS = [
        re.compile(r'\s*PRI\.numTauClass\s*')
        ]
MODEL_PATTERNS = [
        re.compile(r'\s*PRI\.model\s*'),
        ]
TAU_PATTERNS = [
        re.compile(r'\s*PRI\.t\.\d+\s*'),
        ]
D_THETA_PATTERNS = [
        re.compile(r'\s*PRI\.d[12]Theta\.\d+\s*'),
        ]
A_THETA_PATTERNS = [
        re.compile(r'\s*PRI\.aTheta\.\d+\s*'),
        ]
PSI_PATTERNS = [
        re.compile(r'\s*PRI\.Psi\s*'),
        ]
MEAN_TAU_PATTERNS = [
        re.compile(r'\s*PRI\.E\.t\s*'),
        ]
OMEGA_PATTERNS = [
        re.compile(r'\s*PRI\.omega\s*'),
        ]
HEADER_PATTERN = re.compile(r'^\s*\D.+')

##############################################################################
## functions for manipulating prior files

def parse_header(file_obj, sep='\t'):
    file_stream, close = process_file_arg(file_obj, 'rU')
    header = file_stream.next().strip().split(sep)
    if close:
        file_stream.close()
    else:
        file_stream.seek(0)
    return header

def get_parameter_indices(header_list, parameter_patterns=PARAMETER_PATTERNS):
    return get_indices_of_patterns(header_list, parameter_patterns)

def get_stat_indices(header_list, stat_patterns=DEFAULT_STAT_PATTERNS):
    if not stat_patterns:
        stat_patterns = ALL_STAT_PATTERNS
    return get_indices_of_patterns(header_list, stat_patterns)

def get_dummy_indices(header_list, dummy_patterns=DUMMY_PATTERNS):
    return get_indices_of_patterns(header_list, dummy_patterns)
    
def observed_stats_for_abctoolbox(in_file, out_file,
        stat_patterns=DEFAULT_STAT_PATTERNS):
    header = parse_header(in_file)
    indices = get_stat_indices(header, stat_patterns=stat_patterns)
    reduce_columns(in_file, out_file, indices)
    return [header[i] for i in sorted(indices)]

def observed_parameters_for_abctoolbox(in_file, out_file,
        parameter_patterns=PARAMETER_PATTERNS):
    header = parse_header(in_file)
    indices = get_parameter_indices(header,
            parameter_patterns=parameter_patterns)
    reduce_columns(in_file, out_file, indices)
    return [header[i] for i in sorted(indices)]

# def observed_for_msreject(in_file, out_file,
#         stat_patterns=DEFAULT_STAT_PATTERNS,
#         parameter_patterns=PARAMETER_PATTERNS,
#         dummy_patterns=DUMMY_PATTERNS):
#     # in_file, close_in = process_file_arg(in_file, 'rU')
#     # out_file, close_out = process_file_arg(out_file, 'w')
#     header = parse_header(in_file)
#     parameter_indices = get_parameter_indices(header,
#             parameter_patterns=parameter_patterns)
#     stat_indices = get_stat_indices(header,
#             stat_patterns=stat_patterns)
#     dummy_indices = get_dummy_indices(header,
#             dummy_patterns=DUMMY_PATTERNS)
#     indices = sorted(dummy_indices + parameter_indices + stat_indices)
#     reduce_columns(in_file, out_file, indices)
#     # new_head = [header[i] for i in (dummy_indices + parameter_indices + stat_indices)]
#     # out_file.write('%s\t\n' % '\t'.join(new_head))
#     # line_iter = iter(in_file)
#     # line_iter.next()
#     # for line_num, line in enumerate(line_iter):
#     #     l = line.strip().split()
#     #     new_line = ['0', '1', '0', '1', '0'] + [l[i] for i in stat_indices]
#     #     out_file.write('%s\n' % '\t'.join(new_line))

def prior_for_abctoolbox(in_file, out_file,
        stat_patterns=DEFAULT_STAT_PATTERNS,
        parameter_patterns=PARAMETER_PATTERNS):
    header = parse_header(in_file)
    indices = get_parameter_indices(header,
            parameter_patterns=parameter_patterns)
    indices.extend(get_stat_indices(header, stat_patterns=stat_patterns))
    reduce_columns(in_file, out_file, sorted(indices))
    return [header[i] for i in sorted(indices)]

def prior_for_msreject(in_file, out_file,
        stat_patterns=DEFAULT_STAT_PATTERNS,
        parameter_patterns=PARAMETER_PATTERNS,
        dummy_patterns=DUMMY_PATTERNS,
        include_header=False):
    header = parse_header(in_file)
    in_file, close = process_file_arg(in_file)
    indices = get_parameter_indices(header,
            parameter_patterns=parameter_patterns)
    indices.extend(get_stat_indices(header, stat_patterns=stat_patterns))
    indices.extend(get_dummy_indices(header, dummy_patterns=DUMMY_PATTERNS))
    if not include_header:
        in_file.next()
    reduce_columns(in_file, out_file, sorted(indices), extra_tab=True)
    if close:
        in_file.close()
    return [header[i] for i in sorted(indices)]


##############################################################################
## Base class for all workers

class Worker(object):
    total = 0
    def __init__(self,
            temp_fs,
            stdout_path = None,
            stderr_path = None):
        self.__class__.total += 1
        self.temp_fs = temp_fs
        self.stdout_path = stdout_path
        self.stderr_path = stderr_path
        self.cmd = []
        self.process = None
        self.finished = False
        self.exit_code = None
        self.std_out = None
        self.std_err = None

    def get_stderr(self):
        if not self.stderr_path:
            return self.std_err
        try:
            return open(self.stderr_path, 'rU').read()
        except IOError, e:
            _LOG.error('Could not open stderr file')
            raise e

    def start(self):
        _LOG.info('Starting process with following command:\n\t'
                '{0}'.format(' '.join(self.cmd)))
        if self.stdout_path:
            sout = open(self.stdout_path, 'w')
        else:
            sout = subprocess.PIPE
        if self.stderr_path:
            serr = open(self.stderr_path, 'w')
        else:
            serr = subprocess.PIPE
        self.process = subprocess.Popen(self.cmd,
                stdout = sout,
                stderr = serr,
                shell = False)
        self.std_out, self.std_err = self.process.communicate()
        self.exit_code = self.process.wait()
        if self.stdout_path:
            sout.close()
        if self.stderr_path:
            serr.close()
        if self.exit_code != 0:
            if self.stderr_path:
                stderr = open(self.stderr_path, 'rU').read()
            _LOG.error('execution failed')
            raise WorkerExecutionError('{0} ({1}) failed. stderr:\n{2}'.format(
                self.name, self.pid, stderr))
        try:
            self._post_process()
        except:
            e = StringIO()
            traceback.print_exc(file=e)
            _LOG.error('Error during post-processing:\n{0}'.format(
                    e.getvalue()))
            raise
        self.finished = True

    def _post_process(self):
        pass


##############################################################################
## msBayes class for generating prior files

class MsBayesWorker(Worker):
    count = 0
    valid_schemas = ['msreject'] #, 'abctoolbox']

    def __init__(self,
            temp_fs,
            sample_size,
            config_path,
            exe_path = None,
            model_index = None,
            sort_index = None,
            report_parameters = True,
            seed = None,
            observed = False,
            schema = 'msreject',
            stat_patterns=DEFAULT_STAT_PATTERNS,
            parameter_patterns=PARAMETER_PATTERNS,
            stdout_path = None,
            stderr_path = None):
        Worker.__init__(self, temp_fs,
                stdout_path = stdout_path,
                stderr_path = stderr_path)
        self.__class__.count += 1
        self.name = 'MsBayesWorker-' + str(self.count)
        self.sample_size = int(sample_size)
        self.config_path = expand_path(config_path)
        self.output_dir = self.temp_fs.create_subdir(prefix=self.name)
        if not exe_path:
            exe_path = os.path.join(BIN_DIR, 'msbayes.pl')
        self.exe_path = expand_path(exe_path)
        self.model_index = None
        if model_index != None:
            self.model_index = int(model_index)
        self.sort_index = None
        if sort_index != None:
            self.sort_index = int(sort_index)
        self.report_parameters = report_parameters
        if seed is None:
            self.seed = get_random_int()
        else:
            self.seed = int(seed)
        self.prior_path = self.temp_fs.get_file_path(
                parent = self.output_dir,
                prefix = 'prior-{0}-{1}.'.format(
                        self.sample_size,
                        self.seed),
                create = False)
        self.header_path = self.temp_fs.get_file_path(
                parent = self.output_dir,
                prefix = 'prior-{0}-{1}-header.'.format(
                        self.sample_size,
                        self.seed),
                create = False)
        if not schema.lower() in self.valid_schemas:
            raise ValueError(
                    'schema {0} is not valid. Options are: {1}'.format(
                        schema, ','.join(self.valid_schemas)))
        self.schema = schema.lower()
        self.observed = observed
        self.stat_patterns = stat_patterns
        self.parameter_patterns = parameter_patterns
        self.header = None
        self.parameter_indices = None
        self.stat_indices = None
        self._update_cmd()

    def compose_msg(self, msg):
        return '{0}: {1}'.format(self.name, msg)

    def _update_cmd(self):
        cmd = [self.exe_path,
               '-r', str(self.sample_size),
               '-c', self.config_path,
               '-o', self.prior_path,
               '-S', str(self.seed),]
        if self.sort_index != None:
            cmd.extend(['-s', str(self.sort_index)])
        if self.model_index != None:
            cmd.extend(['-m', str(self.model_index)])
        if self.report_parameters:
            cmd.append('-p')
        self.cmd = cmd

    def _post_process(self):
        raw_prior_path = self.prior_path + '.raw'
        shutil.move(self.prior_path, raw_prior_path)
        if self.schema == 'msreject':
            header = prior_for_msreject(
                    in_file = raw_prior_path,
                    out_file = self.prior_path,
                    stat_patterns = self.stat_patterns,
                    parameter_patterns = self.parameter_patterns,
                    dummy_patterns = DUMMY_PATTERNS,
                    include_header = False)
        os.remove(raw_prior_path)
        if header:
            out = open(self.header_path, 'w')
            out.write('{0}\n'.format('\t'.join(header)))
            out.close()
            self._set_header(header)

    def _set_header(self, header):
        self.header = header
        self.parameter_indices = get_parameter_indices(
                header_list = self.header,
                parameter_patterns = PARAMETER_PATTERNS)
        self.stat_indices = get_stat_indices(
                header_list = self.header,
                stat_patterns = ALL_STAT_PATTERNS)

        
class MsRejectWorker(Worker):
    count = 0
    def __init__(self,
            exe_path,
            prior_path,
            out_path,
            tolerance,
            stats,
            **kwargs):
        Worker.__init__(self, **kwargs)
        self.__class__.count += 1
        self.name = 'MsRejectWorker-' + str(self.count)
        self.exe_path = e
        self.prior_path = prior_path
        self.out_path = out_path
        self.tolerance = tolerance
        self.stats = stats
        self.kill_received = False

    def run(self):
        time.sleep(120)

