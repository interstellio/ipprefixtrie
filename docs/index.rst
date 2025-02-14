==========================
IPPrefixTrie Documentation
==========================

Release v\ |version|

IPPrefixTrie is a project developed and sponsored by **Interstellio IO** https://www.interstellio.io.
It serves a **dual purpose**—as an **educational resource** and as a **functional library**
for managing and querying IP prefixes using an **IP prefix trie (binary prefix tree)**.
It is licensed under the **GNU Lesser General Public License (LGPL)**.

This implementation is not a Radix tree or Patricia tree; it is a **binary prefix tree**,
meaning it does not use path compression but explicitly represents each bit in the prefix.
This structure is commonly used in networking applications where prefix-based lookups are required.

**Supported Features:**

* IPv4 and Ipv6 prefixes.
* Exact Prefix Matches.
* Longest Prefix Match.
* Or Longer Prefix Matches.
* Metadata per prefix. *(for example your own defined dictionary that could contain paths etc.)*

We welcome anyone who wishes to optimise or introduce other types of trees.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   whatisit
   install
   api
   contrib
   contact