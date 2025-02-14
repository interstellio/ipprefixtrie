# -*- coding: utf-8 -*-
#
# This file is part of IPPrefixTrie.
#
# Copyright (C) 2025 Interstellio IO (PTY) LTD.
#
# IPPrefixTrie is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or any later version.
#
# IPPrefixTrie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with IPPrefixTrie. If not, see https://www.gnu.org/licenses/.

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import multiprocessing
import os
import sys

try:
    import sphinx_rtd_theme   # noqa: F401
    html_theme = "sphinx_rtd_theme"
except ImportError:
    html_theme = 'default'

sys.path.insert(0, os.path.abspath('..'))

from ipprefixtrie import metadata  # noqa: E402

# -- Build tweaks -------------------------------------------------------------

if not sys.platform.startswith('win'):
    multiprocessing.set_start_method('fork')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

# -- Project information ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

_version_components = metadata.version.split('.')

project = metadata.project_no_spaces
copyright = metadata.copyright
author = metadata.author
version = '.'.join(_version_components[0:3])
release = version

# -- General configuration ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

if html_theme == 'sphinx_rtd_theme':
    extensions.append('sphinx_rtd_theme')

templates_path = ['_templates']
exclude_patterns = ['_build', '_newsfragments']

# Intersphinx configuration
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for HTML output --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_show_sourcelink = False
html_favicon = '_static/favicon.png'
html_logo = '_static/logo.png'
html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel further.
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html

html_theme_options = {
}
