#! /usr/bin/env python

import os

from pymsbayes.fileio import open
from pymsbayes.utils import SCRIPTS_DIR

LOCAL_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_DIR = os.path.abspath(os.path.dirname(LOCAL_DIR))
TEST_DATA_DIR = os.path.join(TEST_DIR, "data")
TEST_OUTPUT_DIR = os.path.join(TEST_DIR, "output")

def data_path(filename=""):
    return os.path.join(TEST_DATA_DIR, filename)

def data_stream(filename):
    return open(data_path(filename), 'rU')

def scripts_path(filename=""):
    return os.path.join(SCRIPTS_DIR, filename)

def test_path(filename=""):
    return os.path.join(TEST_DIR, filename)

def output_path(filename=""):
    return os.path.join(TEST_OUTPUT_DIR, filename)

def output_stream(filename):
    return open(output_path(filename), 'w')

def script_path(filename=""):
    return os.path.join(SCRIPTS_DIR, filename)

