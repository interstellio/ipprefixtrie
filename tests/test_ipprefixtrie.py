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
import pytest
from ipprefixtrie import IPPrefixTrie
from ipprefixtrie.exceptions import (InvalidPrefixError,
                                     PrefixNotFoundError)


def test_insert_and_get_exact():
    trie = IPPrefixTrie()

    trie.insert("192.168.1.0/24", {"desc": "Private IPv4 range"})
    trie.insert("10.0.0.0/8", {"desc": " Large Private IPv4 range"})
    trie.insert("2001:db8::/32", {"desc": "Documentation IPv6 range"})

    result1 = trie.get_exact("192.168.1.0/24")
    assert result1 == ("192.168.1.0/24", {"desc": "Private IPv4 range"})

    result2 = trie.get_exact("10.0.0.0/8")
    assert result2 == ("10.0.0.0/8", {"desc": " Large Private IPv4 range"})

    result3 = trie.get_exact("2001:db8::/32")
    assert result3 == ("2001:db8::/32", {"desc": "Documentation IPv6 range"})


def test_get_exact_not_found():
    trie = IPPrefixTrie()

    with pytest.raises(PrefixNotFoundError):
        trie.get_exact("192.168.2.0/24")


def test_get_longest_match():
    trie = IPPrefixTrie()

    trie.insert("192.168.1.0/24", {"desc": "Private IPv4 range"})
    trie.insert("192.168.0.0/16", {"desc": "Larger Private IPv4 range"})

    longest_match = trie.get_longest("192.168.1.100")
    assert longest_match == ("192.168.1.0/24", {"desc": "Private IPv4 range"})


def test_get_longest_no_match():
    trie = IPPrefixTrie()

    assert trie.get_longest("10.10.10.10") is None


def test_insert_invalid_prefix():
    trie = IPPrefixTrie()

    with pytest.raises(InvalidPrefixError):
        trie.insert("invalid_prefix")


def test_delete_prefix():
    trie = IPPrefixTrie()

    trie.insert("192.168.1.0/24")
    assert trie.delete("192.168.1.0/24") is True

    with pytest.raises(PrefixNotFoundError):
        trie.get_exact("192.168.1.0/24")


def test_delete_nonexistent_prefix():
    trie = IPPrefixTrie()
    with pytest.raises(PrefixNotFoundError):
        trie.delete("10.10.10.0/24")


def test_get_orlonger():
    trie = IPPrefixTrie()

    trie.insert("192.168.1.0/24", {"desc": "Private IPv4 range"})
    trie.insert("192.168.1.128/25", {"desc": "More specific IPv4 range"})
    trie.insert("2001:db8::/32", {"desc": "IPv6 Documentation Range"})

    results = list(trie.get_orlonger("192.168.1.0/24"))
    assert len(results) == 2
    assert ("192.168.1.0/24",
            {"desc": "Private IPv4 range"}) in results
    assert ("192.168.1.128/25",
            {"desc": "More specific IPv4 range"}) in results

    results = list(trie.get_orlonger("10.0.0.0/8"))
    assert len(results) == 0  # No matching entries

    results = list(trie.get_orlonger("2001:db8::/32"))
    assert len(results) == 1
    assert ("2001:db8::/32", {"desc": "IPv6 Documentation Range"}) in results
