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
from typing import Any
from typing import Generator
import ipaddress

from .exceptions import (InvalidPrefixError,
                         PrefixNotFoundError)


class _IPPrefixTrieNode(object):
    """
    Internal node class for the IPPrefixTrie.

    Attributes:
        left (_IPPrefixTrieNode): Left child node.
        right (_IPPrefixTrieNode): Right child node.
        is_prefix (bool): Indicates if the node represents a valid prefix.
        metadata (Any): Metadata associated with the prefix.
    """
    __slots__ = ("left", "right", "is_prefix", "metadata")

    def __init__(self):
        self.left = None
        self.right = None
        self.is_prefix = False
        self.metadata = None


def _iterate_bits(data: bytes) -> Generator[tuple[int, int, bytes],
                                            None, None]:
    len_in_bytes = len(data)                  # Length of the data in bytes.
    matched_bytes = bytearray(len_in_bytes)   # Ensure full-length padding.

    for bit_pos in range(len_in_bytes * 8):
        byte_index = bit_pos // 8       # Get Byte
        bit_index = 7 - (bit_pos % 8)   # Get Bit in Byte
        bit = (data[byte_index] >> bit_index) & 1

        # Preserve the exact bytes for the matched prefix
        matched_bytes[byte_index] |= (bit << bit_index)

        # Yielding bit position, actual bit and matched bytes thus far.
        yield bit_pos, bit, bytes(matched_bytes)


class IPPrefixTrie(object):
    """
    A binary trie for storing and searching IP prefixes efficiently.
    """
    __slots__ = ("__ipv4_root", "__ipv6_root")

    def __init__(self):
        self.clear()

    def clear(self):
        """Initializes an IP prefix trie.

        Separate roots for IPv4 and IPv6 prefixes.
        """
        self.__ipv4_root = _IPPrefixTrieNode()
        self.__ipv6_root = _IPPrefixTrieNode()

    def insert(self, prefix: str, metadata=None) -> None:
        """Inserts an IP prefix into the trie.

        Args:
            prefix (str): The IPv4 or Ipv6 prefix in CIDR notation.
            raise_error (bool, optional): If True, raises an error if the
                prefix is not found. Defaults to True.

        Raises:
            InvalidPrefixError: If the prefix format is invalid.
        """
        try:
            prefix = ipaddress.ip_network(prefix)
        except ValueError as e:
            raise InvalidPrefixError(str(e)) from None

        prefix_len = prefix.prefixlen
        prefix_bin = prefix.network_address.packed
        if prefix.version == 4:
            node = self.__ipv4_root
        else:
            node = self.__ipv6_root

        for bit_pos, bit, matched_bytes in _iterate_bits(prefix_bin):
            if bit_pos >= prefix_len:
                break
            if bit == 0:  # Insert Left child node.
                if node.left is None:
                    node.left = _IPPrefixTrieNode()
                node = node.left
            elif bit == 1:  # Insert Right child node.
                if node.right is None:
                    node.right = _IPPrefixTrieNode()
                node = node.right

        node.is_prefix = True
        node.metadata = metadata or {}

    def get_exact(self, prefix: str,
                  raise_error=True) -> tuple[str, Any] | None:
        """Retrieves an exact prefix match.

        Args:
            prefix (str): The IPv4 or Ipv6 prefix in CIDR notation.
            raise_error (bool, optional): If True, raises an error if the
                prefix is not found. Defaults to True.

        Raises:
            InvalidPrefixError: If the prefix format is invalid.
            PrefixNotFoundError: If the prefix is not found and
                `raise_error` is True.

        Returns:
            tuple[str, Any] | None: A tuple containing the prefix as a string
            and its associated metadata if found, otherwise None.
        """
        try:
            prefix = ipaddress.ip_network(prefix)
        except ValueError as e:
            raise InvalidPrefixError(str(e)) from None

        prefix_len = prefix.prefixlen
        prefix_bin = prefix.network_address.packed
        if prefix.version == 4:
            node = self.__ipv4_root
        else:
            node = self.__ipv6_root

        # Iterate through each byte in the prefix
        for bit_pos, bit, matched_bytes in _iterate_bits(prefix_bin):
            if bit_pos >= prefix_len:
                break

            if bit == 0:  # Insert Left child node.
                if node.left is None:
                    if raise_error:
                        raise PrefixNotFoundError(str(prefix))
                    return
                node = node.left
            elif bit == 1:  # Insert Right child node.
                if node.right is None:
                    if raise_error:
                        raise PrefixNotFoundError(str(prefix))
                    return
                node = node.right

        if node and node.is_prefix:
            return str(prefix), node.metadata
        elif raise_error:
            raise PrefixNotFoundError(str(prefix))

    def get_longest(self, prefix: str,
                    raise_error=True) -> tuple[str, Any] | None:
        """Finds the longest matching prefix.

        Args:
            prefix (str): The IPv4 or Ipv6 prefix in CIDR notation.
            raise_error (bool, optional): If True, raises an error if the
                prefix is not found. Defaults to True.

        Raises:
            InvalidPrefixError: If the prefix format is invalid.
            PrefixNotFoundError: If the match is not found and
                `raise_error` is True.

        Returns:
            tuple[str, Any] | None: A tuple containing the prefix as a string
            and its associated metadata if found, otherwise None.
        """
        try:
            prefix = ipaddress.ip_network(prefix)
        except ValueError as e:
            raise InvalidPrefixError(str(e)) from None

        prefix_bin = prefix.network_address.packed

        if prefix.version == 4:
            node = self.__ipv4_root
        else:
            node = self.__ipv6_root

        longest_match_node = None
        longest_match_length = 0

        for bit_pos, bit, matched_bytes in _iterate_bits(prefix_bin):
            if bit == 0:
                if node.left is None:
                    break
                node = node.left
            else:
                if node.right is None:
                    break
                node = node.right

            if node.is_prefix:
                longest_match_node = node
                longest_match_length = bit_pos + 1

        if longest_match_node:
            network_address = ipaddress.ip_address(bytes(matched_bytes))
            prefix_str = f"{network_address}/{longest_match_length}"
            return prefix_str, longest_match_node.metadata

        return None

    def get_orlonger(self, prefix: str) -> Generator[tuple[str, Any],
                                                     None, None] | None:
        """Yields orlonger prefixes.

        Args:
            prefix (str): The IPv4 or Ipv6 prefix in CIDR notation.

        Raises:
            InvalidPrefixError: If the prefix format is invalid.

        Yields:
            tuple: (matching prefix as str, metadata)
        """
        try:
            prefix = ipaddress.ip_network(prefix)
        except ValueError as e:
            raise InvalidPrefixError(str(e)) from None

        prefix_bin = prefix.network_address.packed
        if prefix.version == 4:
            node = self.__ipv4_root
        else:
            node = self.__ipv6_root

        matched_bytes = bytearray(len(prefix_bin))
        bit_pos = 0

        # Step 1: Find the given prefix in the trie
        for bit_pos, bit, matched_bytes in _iterate_bits(prefix_bin):
            if bit_pos >= prefix.prefixlen:
                break

            if bit == 0:  # Insert Left child node.
                if node.left is None:
                    return
                node = node.left
            elif bit == 1:  # Insert Right child node.
                if node.right is None:
                    return
                node = node.right

        # Step 2: Traverse tree to yield all and more specific (child) prefixes
        queue = [(node, bit_pos, matched_bytes[:])]
        while queue:
            node, bit_pos, matched_prefix = queue.pop(0)

            if node.is_prefix:
                network_address = ipaddress.ip_address(bytes(matched_prefix))
                yield f"{network_address}/{bit_pos}", node.metadata

            if bit_pos < prefix.max_prefixlen:
                byte_index = bit_pos // 8
                bit_index = 7 - (bit_pos % 8)

                if node.left:
                    left_prefix = bytearray(matched_prefix)
                    left_prefix[byte_index] &= ~(1 << bit_index)
                    queue.append((node.left, bit_pos + 1, left_prefix))

                if node.right:
                    right_prefix = bytearray(matched_prefix)
                    right_prefix[byte_index] |= (1 << bit_index)
                    queue.append((node.right, bit_pos + 1, right_prefix))

    def delete(self, prefix: str, raise_error=True) -> bool:
        """Deletes the given prefix from the trie.

        If it has no children it will clean up nodes up to the
        next valid prefix.

        Args:
            prefix (str): The IPv4 or Ipv6 prefix in CIDR notation.
            raise_error (bool, optional): If True, raises an error if the
                prefix is not found. Defaults to True.

        Raises:
            InvalidPrefixError: If the prefix format is invalid.
            PrefixNotFoundError: If the match is not found and
                `raise_error` is True.

        Returns:
            bool: True if deleted, false is not found.
        """
        try:
            prefix = ipaddress.ip_network(prefix)
        except ValueError as e:
            raise InvalidPrefixError(str(e)) from None

        prefix_bin = prefix.network_address.packed
        if prefix.version == 4:
            node = self.__ipv4_root
        else:
            node = self.__ipv6_root

        path_traversed = []  # Stores nodes visited along the path.

        for bit_pos, bit, matched_bytes in _iterate_bits(prefix_bin):
            if bit_pos >= prefix.prefixlen:
                break

            # Store node reference and bit direction in traversed path.
            path_traversed.append((node, bit))

            if bit == 0:
                if node.left is None:
                    if raise_error:
                        raise PrefixNotFoundError(str(prefix))
                    return False  # Prefix not found
                node = node.left
            else:
                if node.right is None:
                    if raise_error:
                        raise PrefixNotFoundError(str(prefix))
                    return False  # Prefix not found
                node = node.right

        if not node.is_prefix:
            if raise_error:
                raise PrefixNotFoundError(str(prefix))

            return False  # Prefix not found

        # Unset the prefix flag and remove metadata
        node.is_prefix = False
        node.metadata = None

        # Cleanup unnecessary nodes
        while path_traversed:
            parent, bit = path_traversed.pop()
            if (bit == 0 and parent.left
                    and not parent.left.is_prefix
                    and not parent.left.left
                    and not parent.left.right):
                parent.left = None
            elif (bit == 1 and parent.right
                    and not parent.right.is_prefix
                    and not parent.right.left
                    and not parent.right.right):
                parent.right = None
            else:
                break  # Stop cleanup if we hit a valid prefix

        return True
