# Networking Concepts

## OSI model
The Open System Interconnection (OSI) model is a standard for how computers, servers, and people communicate within a system.
The OSI model provides a universal language for describing networks and thanking about them in discrete chunks, or layers.

### Layer 7. Application Layer
- **Purpose**: Provides network services directly to user applications. This is where applications interact with the network
- Examples: `HTTP/HTTPS`, `SSH`, `DNS`, `FTP` etc.

### Layer 6. Presentation Layer
- **Purpose**: Handling data formatting, encryption, and compression. Makes sure sender and receiver understand the data format.
- **Examples**: 
  - TLS/SSL encryption
  - JSON,XML format
  - Data encoding
- TLS encryption happens at presentation layer

### Layer 5. Session Layer
- **Purpose**: Establishes, manages, and terminates connections between systems. Maintains session state.
- **Examples**:
  - SSH session
  - Database Session
  - API session

### Layer 4. Transport Layer
- **Purpose**: Ensure reliable communication and manages ports. 
  - Handles port numbers, reliable delivery, error recovery
  - Protocols: TCP, UDP
- We can use `ss -tulnp` command to check all listening ports

### Layer 3. Network Layer
- **Purpose**: Handles IP addressing and routing between networks. Responsible for delivering packets across networks.
  - Protocol: `IP`
  - Devices: Routers

### Layer 2. Data Link Layer
- **Purpose**: Handles communication within the same local network using MAC addresses. Ensure data reaches correct device in LAN.
  - Uses: MAC addresses, Ethernet
- Commands to trouble shoot: `ip link`, `ip neigh`, `arp -a`

### Layer 1. Physical Layer
- **Purpose**: Handles physical transmission of data
- **Examples**: 
  - Network cables
  - Network Cards

---

## TCP/IP model
The TCP/IP model is a 4-layer networking framework that standardizes data transmission. It enables internet communication by organizing protocols into functional layers, ranging from user applications (HTTP, DNS) down to physical hardware transmission (Ethernet)

- **Application Layer (Top)**: Interfaces with applications, handles data formatting, and manages user sessions
  - Protocols: HTTP/HTTPS(web), FTP(files), SMTP/IMAP/POP3(email), DNS, SSH/Telnet(remote access)
- **Transport Layer**: Provides end-to-end communication, flow control, and error correction.
  - Protocols: TCP(reliable, connection-oriented), UDP (fast, connection less).
- **Internet Layer**: Handles logical addressing and routing packets across networks.
  - Protocols: IP (IPv4/v6), ICMP(error reporting), ARP
- **Network Access Layer**: Manages physical, hardware-level transmission of data frames
  - Protocols: Ethernet, IP, ARP.

---

## TCP & UDP 
- TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are core transport layer protocols in networking.
- TCP is connection oriented, ensuring reliable, ordered, and error-checked data delivery via a three-way handshake.
- UDP is connection-less and faster, prioritizing speed over guaranteed delivery, making it ideal for real-time applications.

### Key Differences
- **Connection**: TCP used 3-way handshake to establish connection before sending data. UDP is connection less and sends data directly
- **Reliable**: TCP guarantees delivery, acknowledging(ACK) received packets and retransmitting lost ones. UDP does not guarantee delivery; packets may be lost.
- **Ordering**: TCP ensures packets are reassembled in the correct order. UDP packets are independent and may arrive out of order.
- **Speed**: UDP is faster due to lower overhead and no need for acknowledgement
- **Use Cases (TCP)**: Web Browsing (HTTP/ HTTPS), email (SMTP/IMAP/POP3), file transfer(FTP) and secure data transfer.
- **Use Cases (UDP)**: Live Video Streaming, voice calls(VoIP), online gaming and DNS

---

## How does SSL work? SSL certificates & TLS

### What is SSL
SSL stands for Secure Sockets Layer, and is refers to a protocol for encrypting, securing, and authenticating communications that take place on the internet. Although SSL was replaced by an updated protocol calls TLS (Transport Layer Security) some time ago, "SSL" is still a commonly used term for this technology.

### The TLS handshake
TLS communication sessions begin with a TLS handshake. A TLS handshake used something called asymmetric encryption, meaning that two different keys are used on the two ends of the conversation. This is possible because of a technique called public key cryptography

In public key cryptography, two keys are used: a public key, which the server makes available publicly, and a private key, which is kept secret and only used on the server side. Data encryption with the public key can only be decrypted with the private key.

During TLS handshake, the client and server use the public and private keys to exchange randomly generated data, and this random data is used to create new keys for encryption, called session keys.

### Symmetric encryption with session keys
Unlike asymmetric encryption, in symmetric encryption the two parties in a conversation use the same key. After the TLS handshake, both sides use the same keys for encryption.

Once session keys are in use, the public and private keys are not used anymore. Session keys are temporary keys that are not used again once the session is terminated. A new, random set of session keys will be created for next session.

### What is SSL Certificate
An SSL Certificate is a file installed on a website's origin server. It;s simply a data file containing the public key and the identity of the website owner, along with other information.
With out an SSL certificate, a website's traffic can't be encrypted with TLS.

Technically, any website owner can create their own SSL certificate, and such certificates are called self-signed certificates. However, browsers do not consider self-signed certificates to be as thrust worthy as SSL certificates issued by a certificate authority.

### Step-by-Step TLS Handshake
1. **Client Hello (Browser -> Server)**
Browser Sends:
   - Supported TLS versions
   - Supported cipher suites
   - Random number (Client Random)
   - SNI (server name)
2. **Server Hello (Server -> Browser)**
Server responds with:
   - Selected TLS version
   - Selected cipher suite
   - Server Random
   - SSL/TLS certificate
3. **Browser Validates the Certificate**
Browser Checks:
   - Is the certificate expired?
   - Does the domain match?
   - Is it signed by a trusted CA?
   - Is the CA in my trust store>
- If Validation Fails, Browser sends a warning message.
4. **Key Exchange Happens**
   - Browser generates a pre-master secret
   - Encrypt it using the server's public key.
   - Sends it to server
   - Server decrypts using its private key.


---

## IP Addressing
IP addressing, specificaly IPv4, uses 32-bit addresses often expressed in decimals, categorized into public (internet-routable) and private (internal) ranges.

Subnetting divides these networks into smaller, manageable chunks using CIDR (classless Inter-Domain Routing) notation (*.*.*.*/n), where `/n` denotes the number of fixed network bit, allowing flexible, efficient allocation of IP space.

### Public vs Private IP Addresses
- **Private IPs**: Used for internal networking. They are not routed on the public internet
  - Ranges `10.0.0.0/8`
  - Ranges `172.16.0.0/12`
  - Ranges `196.168.0.0/16`
- **Public IPs**: Globally unique addresses routable over the internet.

### IPv4 address classes and reserved ranges
IP addresses are typically made of two separate components. 
- The first part of the address is used to identify the network that the address is part of.
- The part that comes afterwards is used to specify a specific host within that network

IPv4 addresses are traditionally divided into five different classes, named A through E, meant to differentiate segments of the available addressable IPv4 space.

- **Class A**:
  - `0___`: If the first bit of an IPv4 address is `0`, this means that the address is part of class A. This means that any address from `0.0.0.0` to `127.255.255.255` is in Class A
- **Class B**:
  - `10__`: Class B indicates any address from `128.0.0.0` to `191.255.255.255`. This represents the addresses that have a `1` for their first bit, but don't have a `1` for their second bit
- **Class C**:
  - `110_`: Class C is defined as the addresses ranging from `192.0.0.0` to `223.225.225.225`. This represents all of the addresses with a `1` in first two bits
- **Class D**
  - `1110`: This class includes addresses that have `111` as their first three bits. This addresses ranges from `224.0.0.0` to `239.225.225.225`
- **Class E**
  - `1111`: This class defines addresses between `240.0.0.0` to `255.255.255.255`


### Reserved Private Ranges
There are also some portions of IPv4 space that are reserved for specific uses.

1. One of the most useful reserved ranges is the loopback range specified by addresses from `127.0.0.0` to `127.255.255.255` This range is used by each host to test networking to itself
2. Each of the normal classes also have a range within them that is used to designate private network addresses.
   1. For class A `10.0.0.0` to `10.255.255.255` CIDR `10.0.0.0/8`
   2. For class B `172.16.0.0` to `172.31.255.255` CIDR `172.16.0.0/12`
   3. For Class C, `192.16.0.0` to `192.16.255.255` CIDR `192.16.0.0/16`

### CIDR notation
A system called Classless Inter-Domain Routing, or CIDR, was developed as an alternative to traditional subnetting. The idea is that you can add a specification in the IP address itself as to the number of significant bits that make up the routing or network portion.

For example, e could express the idea that the IP address `192.168.0.15` is associated with the netmask `255.255.255.0` by using the CIDR notation of `192.168.0.15/24`. This means that the first 24 bits of the IP address given are considered significant for the network routing.

This allows us some interesting possibilities. We can use these to reference "supernets".  In this case, we mean a more inclusive range that not possible with a traditional subnet mask.

For instance, In a class C network, like above, we could not combine the addresses from the networks `192.168.0.0` and `192.168.1.0` because the netmask for the class C addresses is `255.255.255.0`

However, using CIDR notation, we can combine these blocks by referencing this chunk as `192.168.0.0/23`. This specifies that there are 23 bits used for the network portion that we are referring to.

So first network `192.168.0.0` could be represented as 
`1100 0000 - 1010 1000 - 0000 0000 - 0000 0000`

While the second network `192.168.1.0` could be represented as
`1100 0000 - 1010 1000 - 0000 0001 - 0000 0000`

The CIDR address we specified indicates that the first 23 bits are used for the networking block we are referring. This is equivalent to subnet mask `255.255.254.0` or
`1111 1111 - 1111 1111 - 1111 1110 - 0000 0000`


---

## DNS Resolution Process

The DNS resolution process translates human-readable domain names into IP addresses through a hierarchical lookup involving DNS recursors, root servers, TLD servers and authoritative name servers.

### The resolution process
1. **User Request**: A user types a domain name into their web browser
2. **Recursive Resolver Check**: The request goes to a DNS recursive resolver (usually managed by ISP), which first checks its local cache
3. **Root Server query**: If not cached, the resolver queries a Root Server, which directs it to the Top-Level Domain (TLD) server
4. **TLD server query**: The TLD server directs the resolver to the domain's Authoritative Name Server.
5. **Authoritative Name Server**: The authoritative name server looks up the IP address for the domain, usually A or AAAA record.
6. **Return IP and Cache**: The resolver returns the IP address to the browser, which loads the site, and caches the result for the future use based on the TTL.

### DNS Record
DNS Records (aka zone files) are instructions that live in authoritative DNS servers are provided information about a domain including what IP address is associated with that domain and how to handle requests for that domain.
These records consists of series of text file written in what is known as DNS syntax.
All domains are required to have at least a few essential DNS records for a user to be access their website using a domain name, and there are several optional records that server additional purpose.

### Common types of DNS Records
- **A record**: The record that holds the IP address of a domain
- **AAAA record**: The record contains the IPv6 address for a domain (as opposed to A record, which list the IPv4 address)
- **CNAME record**: Forwards one domain or subdomain to another domain, does NOT provide an IP address.
- **MX record**: Directs mail to an email server
- **TXT record**: Lets an admin store text notes in the record. These records are often used for email security
- **NS record**: Stores the name server for a DNS entry
- **SOA record**: Stores admin information about a domain
- **SRV record**: Specifies a port for specific services
- **PTR record**: Provides a domain name in reverse-lookups.


---

## Default Gateway & Routing
A default gateway is the node (usually a router) on a computer network that serves as the exit point, directing traffic to other networks, such as the internet, when the destination is outside the local subnet. It acts as a bridge, allowing local devices to communicate with external networks.

### How Routing happens
1. **Destination Check**: When a device sends data, it first checks if the destination IP address is within its own local subnet.
2. **Local Delivery**: If the destination is on the same local network, the data is sent directly.
3. **Forwarding to Gateway**: If the destination is outside the local network, the device forwards the packet to the configured default gateway (router)
4. **Routing Decision**: The router receives the packet and uses its routing table to determine the best path to the destination network, often passing it through other routers (a "hop-by-hop" process) until it reaches the destination.
5. **Internet Access**: For home networks, the wifi router is typically the default gateway that handles all internet-bound traffic.