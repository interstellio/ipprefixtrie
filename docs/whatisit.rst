What is IP Prefix Trees
=======================

An IP Prefix Trie (also called an IP prefix tree) is a data structure used for efficiently storing and retrieving IP address prefixes. It is a type of binary trie that organises IP prefixes hierarchically by their binary representation.

In networking, an IP prefix represents a range of IP addresses, typically written in CIDR notation (e.g., 192.168.1.0/24). A prefix trie allows for fast lookups, longest prefix matching (LPM), and efficient storage of multiple prefixes in a structured manner.


Why Use an IP Prefix Trie?
--------------------------

**IP prefix tries are widely used in networking applications, including:**

* **Routing Tables** – These are used in routers to determine the next hop for forwarding packets.
* **Firewall and ACL Rules** – Helps efficiently match incoming traffic against security rules.
* **IP Address Management** – Organizes and assigns subnets efficiently.
* **Content Delivery Networks (CDNs)** – Determine the nearest server for a client request.

How Does an IP Prefix Trie Work?
--------------------------------

An IP prefix trie represents IP addresses as binary values, with each bit determining a left (0) or right (1) branch in the trie.

**Given the following prefixes:**

.. code::

    192.168.1.0/24
    10.0.0.0/8
    2001:db8::/32 (IPv6)

**The binary representation of the first few bits would be:**

.. code::

    192.168.1.0/24  ->  11000000 10101000 00000001 00000000
    10.0.0.0/8      ->  00001010 00000000 00000000 00000000
    2001:db8::/32   ->  00100000 00000001 00001101 10111000 00000000 ...

**The IPv4 trie structure organises these as follows:**

.. code::

        (root)
        /    \
    (10/8)  (192/24)

Each node represents a bit in the prefix, with paths leading to a stored prefix.

Different Types of Prefix Tries
-------------------------------

1. Binary Trie (Basic IP Prefix Trie)
    * Each node has at most two children (0 and 1 for each bit).
    * Used in basic prefix matching.
2. Radix Trie (Compressed Trie)
    * Compresses common paths to reduce memory usage.
    * Often used in high-performance routers.
3. Patricia Trie (Practical Algorithm to Retrieve Information Coded in Alphanumeric)
    * A space-efficient variation of the binary trie.
    * Stores only branching points, improving efficiency.

Example Use Case: Longest Prefix Matching (LPM)
-----------------------------------------------

Longest prefix matching is a critical function in routing:

**Example table:**

.. code::

    Prefix        Next Hop
    --------------------------------
    192.168.1.0/24   Router A
    192.168.0.0/16   Router B
    0.0.0.0/0        Default Gateway

**Lookup 192.168.1.50:**

1. Matches 0.0.0.0/0 (default gateway)
2. Matches 192.168.0.0/16
3. Matches 192.168.1.0/24 (Longest Match)
4. Forward to Router A.

How Can This Help in Python Projects?
--------------------------------------

* **Network Tools** – Build software-defined networking (SDN) tools.
* **Security Applications** – Implement intrusion detection and firewalls.
* **Load Balancers & Proxies** – Optimize traffic distribution.
* **Internet Traffic Analysis** – Study network flows and patterns.

IPPrefixTrie project provides an easy-to-use Python implementation of an IP prefix trie, useful for learning and real-world applications.
