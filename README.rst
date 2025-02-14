============================
IPPrefixTrie
============================

**Current Version: 1.0.0**

IPPrefixTrie is a project developed and sponsored by **Interstellio IO**.
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

**Documentation:** https://ipprefixtrie.readthedocs.io

-------------------------------------------------
Installation
-------------------------------------------------
To install the IPPrefixTrie module, use the following command:

.. code-block:: bash

    pip install ipprefixtrie

-------------------------------------------------
Usage
-------------------------------------------------
Here’s a quick example of how to use the **IPPrefixTrie** module:

.. code-block:: python

    from ipprefixtrie import IPPrefixTrie

    trie = IPPrefixTrie()
    trie.insert("192.168.1.0/24", {"desc": "Private IPv4 range"})
    trie.insert("2001:db8::/32", {"desc": "Documentation IPv6 range"})

    # Lookup an exact prefix
    print(trie.get_exact("192.168.1.0/24"))  # Returns: ('192.168.1.0/24', {'desc': 'Private IPv4 range'})

    # Get longest matching prefix
    print(trie.get_longest("192.168.1.100"))  # Returns: ('192.168.1.0/24', {'desc': 'Private IPv4 range'})

    # Find more specific prefixes
    print(list(trie.get_orlonger("192.168.1.0/24")))

-------------------------------------------------
What is a Binary Prefix Tree?
-------------------------------------------------
A **binary prefix tree** is a data structure designed for prefix-based searching.
Each node in the tree represents a bit of an IP address, making it well-suited
for **longest prefix match (LPM)** operations, commonly used in **network routing,
firewall rules, and access control lists (ACLs)**.

Unlike **Radix** or **Patricia** trees, a binary prefix tree maintains an explicit
path for every bit in the IP address, making it more straightforward but potentially
more significant in memory footprint. This makes it useful for **both practical
implementations and educational learning**, where a clear and intuitive understanding
of IP prefix operations is required.


-------------------------------------------------
Educational and Practical Purpose
-------------------------------------------------
This project is also designed for **learning and experimentation** with IP
prefix management while also serving as a practical tool for prefix-based
lookups. While **not optimised for high-performance production
environments**, it serves as an excellent reference for:

- Understanding **network prefix matching** in **Python**.
- Exploring how **trie-based data structures** work.
- Implementing **basic networking concepts** like **routing tables and firewall rules**.

-------------------------------------------------
License
-------------------------------------------------
IPPrefixTrie is released under the **LGPL License**, meaning you are free to use, modify, and distribute it under the terms of the **GNU Lesser General Public License**.

For more details, see: https://www.gnu.org/licenses/lgpl-3.0.html

-------------------------------------------------
Contributing
-------------------------------------------------
Contributions to this project are welcome! If you'd like to report issues or suggest improvements, please submit a pull request or open an issue on the repository.

All code should follow the PEP-8 standard as outlined here: https://peps.python.org/pep-0008/

-------------------------------------------------
Contact
-------------------------------------------------
For inquiries about **IPPrefixTrie**, please contact **Interstellio IO** at:

Website: [https://www.interstellio.io](https://www.interstellio.io)
Email: opensource@interstellio.io

You can also view the MAINTAINERS file for contacts.