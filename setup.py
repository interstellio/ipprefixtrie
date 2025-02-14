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

# IPPrefixTrie is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with IPPrefixTrie. If not, see https://www.gnu.org/licenses/.

import os
import sys
from importlib.machinery import SourceFileLoader

try:
    from setuptools import setup, find_packages
except ImportError:
    print('Requires `setuptools` to be installed')
    print('`pip install setuptools`')
    exit()

# DEFINE ROOT PACKAGE NAME
PACKAGE = 'ipprefixtrie'

MYDIR = os.path.abspath(os.path.dirname(__file__))
CODE_DIRECTORY = os.path.join(MYDIR, PACKAGE)
sys.path.insert(0, MYDIR)
os.chdir(MYDIR)

# Load Metadata from package.
metadata = SourceFileLoader(
    'metadata', os.path.join(MYDIR, CODE_DIRECTORY,
                             'metadata.py')).load_module()


def requirements(path):
    dependency = []
    if os.path.exists(os.path.join(os.path.dirname(__file__), path)):
        with open(os.path.join(os.path.dirname(__file__), path)) as req:
            dependency = req.read().splitlines()

    return dependency


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


python_version_specific_requires = []
install_requires = requirements('requirements.txt')

# See here for more options:
# <http://pythonhosted.org/setuptools/setuptools.html>
setup_dict = dict(
    name=metadata.package,
    version=metadata.version,
    author=metadata.author,
    author_email=metadata.email,
    maintainer=metadata.author,
    maintainer_email=metadata.email,
    url=metadata.url,
    description=metadata.description,
    long_description=read('README.rst'),
    include_package_data=True,
    classifiers=metadata.classifiers,
    packages=find_packages(exclude=()),
    install_requires=[] + python_version_specific_requires + install_requires,
    zip_safe=False,  # don't use eggs
    python_requires='>=3.8',
)


def main():
    setup(**setup_dict)


if __name__ == '__main__':
    main()
