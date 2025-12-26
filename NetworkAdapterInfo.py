import ifcfg

print("Available Network Adapters and their IP Addresses:")
adapters = ifcfg.interfaces()
for adapter_name, adapter_info in adapters.items():
    
    ip_address = adapter_info.get('inet', 'No IP assigned')
    if(str(ip_address) != "None"):
        print(f"Adapter: {adapter_name}, IP Address: {ip_address}")