import dns
import dns.resolver
import socket
import time

# Target domain
domain = "google.com"

print("=" * 60)
print("DNS OSINT RECON TOOL")
print("=" * 60)
print(f"Target Domain : {domain}")
print()


# Perform a Reverse DNS lookup
def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except socket.herror:
        return []

    return [result[0]] + result[1]


# Query DNS A records
def DNSRequest(domain):
    try:
        result = dns.resolver.resolve(domain, "A")

        addresses = []

        for answer in result:
            ip = answer.to_text()

            addresses.append({
                "domain": domain,
                "ip": ip,
                "reverse_dns": ReverseDNS(ip)
            })

        return addresses

    except (
        dns.resolver.NXDOMAIN,
        dns.resolver.NoAnswer,
        dns.resolver.NoNameservers,
        dns.resolver.LifetimeTimeout,
        dns.exception.Timeout,
    ):
        return []


# Search for subdomains using a wordlist
def SubdomainSearch(domain, dictionary, nums):

    results = []

    for word in dictionary:

        subdomain = word + "." + domain

        results.extend(DNSRequest(subdomain))

        if nums:

            for i in range(10):

                s = word + str(i) + "." + domain

                results.extend(DNSRequest(s))

    return results


# Read the wordlist
d = "subdomains.txt"

with open(d, "r") as f:
    dictionary = f.read().splitlines()


# Start timer
start_time = time.time()


# Perform the scan
results = SubdomainSearch(domain, dictionary, True)


# Stop timer
end_time = time.time()

elapsed_time = end_time - start_time


# Display results
print("\nDiscovered Subdomains")
print("=" * 60)

for item in results:

    print(f"Domain      : {item['domain']}")
    print(f"IP Address  : {item['ip']}")
    print(f"Reverse DNS : {', '.join(item['reverse_dns']) if item['reverse_dns'] else 'None'}")
    print("-" * 60)


# Display summary
print("\n" + "=" * 60)
print("SCAN SUMMARY")
print("=" * 60)
print(f"Target Domain : {domain}")
print(f"Results Found : {len(results)}")
print(f"Scan Time     : {elapsed_time:.2f} seconds")