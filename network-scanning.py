from scapy.all import IP, ICMP, sr1

def ping_host(host):
    """
    Ping a host to check if it is reachable.
    
    :param host: The IP address or hostname of the host to ping.
    :return: True if the host is reachable, False otherwise.
    """
    packet = IP(dst=host)/ICMP()
    response = sr1(packet, timeout=2, verbose=False)
    
    if response :
        return f"Host {host} is online."
    else:
        return f"Host {host} is offline."
    
# Example usage
host_to_scan = "google.com"  # Replace with the host you want to scan
result = ping_host(host_to_scan)
print(result)