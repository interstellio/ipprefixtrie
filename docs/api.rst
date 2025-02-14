Usage Guidelines
================

Example Quickstart
------------------

.. code-block:: python

    from ipprefixtrie import IPPrefixTrie

    trie = IPPrefixTrie()
    trie.insert("192.168.1.0/24", {"desc": "Private IPv4 range"})
    trie.insert("2001:db8::/32", {"desc": "Documentation IPv6 range"})

    # Lookup an exact prefix
    print(trie.get_exact("192.168.1.0/24"))

    # Get longest matching prefix
    print(trie.get_longest("192.168.1.100"))

    # Find all more specific prefixes
    print(list(trie.get_orlonger("192.168.1.0/24")))

    # Delete a prefix
    trie.delete("192.168.1.0/24")

API Reference
-------------

.. autoclass:: ipprefixtrie.IPPrefixTrie
    :members:
    :inherited-members: