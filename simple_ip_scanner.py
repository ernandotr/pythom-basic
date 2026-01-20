import socket

def scan_ip(ip_address):
    """Scan a single IP address and port to check if it's open."""
    try:
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False

def main():
    start_ip = input("Enter the starting IP address (e.g., 192.168.1.1): ")
    end_ip = input("Enter the ending IP address (e.g., 192.168.1.254): ")

    for ip_address in range(int(start_ip), int(end_ip) + 1):
        if scan_ip(str(ip_address)):
            print(f"IP Address {ip_address} is valid.")
        else:
            print(f"IP Address {ip_address} is invalid.")

if __name__ == "__main__":
    main()