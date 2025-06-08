import speedtest as st

def run_speed_test():
    test = st.Speedtest(secure=True)  # Use secure=True for HTTPS connections
    print("Finding best server...")
    best_server = test.get_best_server()  # Automatically finds the best server based on ping
    print(f"Best server found: {best_server['host']} located in {best_server['country']}")
    down_speed = test.download() / 1_000_000  # Convert to Mbps
    print(f"Download Speed: {down_speed:.2f} Mbps")

    up_speed = test.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload Speed: {up_speed:.2f} Mbps")

    ping = test.results.ping  # Ping in ms  
    print(f"Ping: {ping:.2f} ms")

run_speed_test()
