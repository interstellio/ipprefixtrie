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


class Error(Exception):
    """Base class for all project-specific exceptions."""
    pass


class IPPrefixError(Error):
    """Base exception for all IP prefix-related errors."""
    pass


class InvalidPrefixError(IPPrefixError):
    """Raised when an invalid prefix is used."""
    pass


class PrefixNotFoundError(IPPrefixError):
    """Raised when a prefix lookup fails."""
    pass
