# -*- coding: utf-8 -*-
#
# PyMsBayes documentation build configuration file, created by
# sphinx-quickstart on Sat May 17 16:35:13 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import time

from pymsbayes import __version__ as PROJECT_VERSION

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.pngmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'doc'

# General information about the project.
project = u'PyMsBayes'
copyright = u'2013-{0}, Jamie R. Oaks'.format(time.strftime('%Y'))

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = PROJECT_VERSION
# The full version, including alpha/beta/rc tags.
release = PROJECT_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

rst_epilog = """
.. |jro| replace:: Jamie Oaks
.. _jro: http://www.phyletica.com
.. |mth| replace:: Mark T. Holder
.. _mth: http://people.ku.edu/~mtholder

.. |pmb| replace:: PyMsBayes
.. _pmb: http://joaks1.github.io/PyMsBayes/
.. |pmb_gh| replace:: PyMsBayes
.. _pmb_gh: https://github.com/joaks1/PyMsBayes
.. |pmb_home_url| replace:: http://joaks1.github.io/PyMsBayes/
.. |pmb_tutorials_url| replace:: http://joaks1.github.io/PyMsBayes/tutorials/index.html
.. |pmb_gh_url| replace:: https://github.com/joaks1/PyMsBayes
.. |pmb_tutorials_doc| replace:: /tutorials/index
.. |pmb_copyright| replace:: **Copyright 2013-{this_year} Jamie R. Oaks**

.. |python| replace:: Python
.. _python: http://www.python.org/
.. |python27| replace:: Python 2.7
.. _python27: http://www.python.org/download/releases/2.7/
.. |setuptools| replace:: setuptools
.. _setuptools: http://pypi.python.org/pypi/setuptools
.. |pip| replace:: pip
.. _pip: http://pypi.python.org/pypi/pip
.. |git| replace:: Git
.. _Git: http://git-scm.com/
.. |gpl3| replace:: http://www.gnu.org/licenses/gpl-3.0-standalone.html

.. |dpp-msbayes| replace:: dpp-msbayes
.. _dpp-msbayes: https://github.com/joaks1/dpp-msbayes.git
.. |dpp-msbayes-url| replace:: https://github.com/joaks1/dpp-msbayes.git
.. |msbayes| replace:: msBayes
.. _msbayes: http://msbayes.sourceforge.net/
.. |msbayes_url| replace:: http://msbayes.sourceforge.net/
.. |abctb| replace:: ABCtoolbox
.. _abctb: http://www.cmpg.iee.unibe.ch/content/softwares__services/computer_programs/abctoolbox/index_eng.html
.. |abctb_url| replace:: http://www.cmpg.iee.unibe.ch/content/softwares__services/computer_programs/abctoolbox/index_eng.html
.. |eureject| replace:: euReject
.. _eureject: https://github.com/joaks1/abacus.git
.. |abacus| replace:: ABACUS
.. _abacus: https://github.com/joaks1/abacus.git
.. |abacus_url| replace:: https://github.com/joaks1/abacus.git

.. |MsBayesWorker| replace:: :class:`~pymsbayes.workers.MsBayesWorker`
.. |Manager| replace:: :class:`~pymsbayes.manager.Manager`

.. |True| replace:: `True`
.. |False| replace:: `False`
.. |None| replace:: `None`

.. |example-dir| replace:: `PyMsBayes/examples`
.. _example-dir: https://github.com/joaks1/PyMsBayes/tree/master/examples
.. |lizard-dir| replace:: `PyMsBayes/examples/lizards`
.. _lizard-dir: https://github.com/joaks1/PyMsBayes/tree/master/examples/lizards
.. |lizard-seq-dir| replace:: `PyMsBayes/examples/lizards/sequences`
.. _lizard-seq-dir: https://github.com/joaks1/PyMsBayes/tree/master/examples/lizards/sequences
.. |lizard-config-dir| replace:: `PyMsBayes/examples/lizards/configs`
.. _lizard-config-dir: https://github.com/joaks1/PyMsBayes/tree/master/examples/lizards/configs
""".format(this_year = time.strftime('%Y'))

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = 'pymsbayes'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['_themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyMsBayesdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'PyMsBayes.tex', u'PyMsBayes Documentation',
   u'Jamie R. Oaks', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pymsbayes', u'PyMsBayes Documentation',
     [u'Jamie R. Oaks'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'PyMsBayes', u'PyMsBayes Documentation',
   u'Jamie R. Oaks', 'PyMsBayes', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'PyMsBayes'
epub_author = u'Jamie R. Oaks'
epub_publisher = u'Jamie R. Oaks'
epub_copyright = u'2014, Jamie R. Oaks'

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'PyMsBayes'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

#####################################################
# add LaTeX macros 
latex_elements['preamble'] = '\usepackage{amsmath}\n\usepackage{amssymb}\n'

f = file('latex_macros.sty')

try:
    pngmath_latex_preamble  # check whether this is already defined
except NameError:
    pngmath_latex_preamble = ""

for macro in f:
    # used when building latex and pdf versions
    latex_elements['preamble'] += macro + '\n'
    # used when building html version
    pngmath_latex_preamble += macro + '\n'
