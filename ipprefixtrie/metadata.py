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

from datetime import datetime

# The package name, which is also the "UNIX name" for the project.
package = 'ipprefixtrie'
project = 'IPPrefixTrie'
project_no_spaces = project.replace(' ', '')

# Please follow https://www.python.org/dev/peps/pep-0440/
version = '1.0.0'
description = project
author = 'Interstellio IO (PTY) LTD'
email = 'info@interstellio.io'
license = 'LGPLv3'
copyright = '2025-%s %s' % (datetime.now().year, author,)
url = 'https://www.interstellio.io/bgphoria'
identity = project + ' v' + version

# Classifiers
# <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Telecommunications Industry',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.10',
    'Topic :: System :: Networking']
