# pip install wmi
# network_info.py
# This script uses the WMI library to retrieve and display network adapter information on a Windows system 
import wmi

def display_network_info():
    c = wmi.WMI()
    adapters = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)

    if not adapters:
        print("No network adapters found.")
        return

    for adapter in adapters:
        print(f"Description: {adapter.Description}")
        print(f"MAC Address: {adapter.MACAddress}")
        print(f"IP Address: {adapter.IPAddress[0] if adapter.IPAddress else 'N/A'}")
        print(f"Subnet Mask: {adapter.IPSubnet[0] if adapter.IPSubnet else 'N/A'}")
        print(f"Default Gateway: {adapter.DefaultIPGateway[0] if adapter.DefaultIPGateway else 'N/A'}")
        print("-" * 40)

if __name__ == "__main__":
    display_network_info()