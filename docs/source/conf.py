#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# utils3 documentation build configuration file, created by
# sphinx-quickstart on Mon Apr 30 12:29:52 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime as dt

sys.path.insert(0, os.path.realpath('../../dblib'))
from _version import __version__


# -- Project information -----------------------------------------------------

project = 'dblib'
copyright = f'2023-2024 | S3DEV | version {__version__}'
author = 'S3DEV Development Team'
version = __version__
release = __version__


# -- General configuration ---------------------------------------------------

html_theme = 'sphinx_rtd_theme'
#exclude_patterns = ['htg__*.rst', 'auth.rst']
extensions = ['sphinx.ext.autodoc', 
              'sphinx.ext.ifconfig', 
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon', 
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx_copybutton',
              'sphinx_git']
html_copy_source = False
html_css_files = ['css/s5defs-rules.css']
html_logo = '_static/img/s3dev_tri_white_sm.png'
html_static_path = ['_static']
html_search_language = 'en'
html_show_copyright = True
html_show_sourcelink = False
html_show_sphinx = False
html_title = f'{project} - v{__version__} Documentation'
master_doc = 'index'
mathjax_path = 'js/mathjax.js'
numfig = True
pygments_style = 'sphinx'
source_suffix = '.rst'
templates_path = ['_templates']
todo_include_todos = True


# -- Epilog ------------------------------------------------------------------
# These items are included at the end of each source file.
# This is a useful place to keep file paths or variables which are used 
# throughout.

dtme = dt.now().strftime('%d %b %Y')
rst_epilog = f"""

.. |lastupdated| replace:: Last updated: {dtme}

.. include:: _static/css/s5defs.txt

"""

