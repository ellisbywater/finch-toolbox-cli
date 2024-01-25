import dns
import dns.resolver
import socket

class Domain:
    subdomain: str
    ips: [str]

class DNSReconResults:
    target_domain: str
    dns_records: [Domain | None] = []

# IP to domain
# This function takes an IP address as input and returns a list of domains associated with that IP address.
def ReverseDNS(ip: str) -> list:
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0] + result[1]]
    except socket.herror:
        return None
   
# Domain to IP
# This function takes a domain name as input and returns a list of IP addresses associated with that domain.
def FindIPs(domain: str) -> list | None:
    ips: [str] = []
    try:
        result = dns.resolver.resolve(domain)
        if result:
            for answer in result:
                ips.append(answer.to_text())
    except (dns.resolver.NXDOMAIN, dns.resolver.Timeout):
        return None
    return ips

# Full search
# This function takes a domain name as input and returns a list of subdomains associated with that domain.
def ScanAndSearch(domain: str, dictionary: str, nums: bool = False) -> list:
    successes: [Domain] = []
    for word in dictionary:
        subdomain = word+"."+domain
        ips = FindIPs(subdomain)
        if len(ips) > 0:
            successes.append({subdomain, ips})
        if nums:
            for i in range(0,10):
                s = word+str(i)+"."+domain
                ips = FindIPs(s)
                if len(ips) > 0:
                    successes.append({s, ips})
    return successes


def ReverseAndSearch(ip: str, dictionary: str, nums: bool = False) -> list:
    domain = ReverseDNS(ip)
    if domain:
        return ScanAndSearch(domain[0], dictionary, nums)
    return None


