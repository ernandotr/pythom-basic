import psutil, time

before = psutil.net_io_counters()
time.sleep(1)
after = psutil.net_io_counters()

dowload_speed = after.bytes_recv - before.bytes_recv
upload_speed = after.bytes_sent - before.bytes_sent 

print(f"{'Download Speed (bytes/s)':<30} {'Upload Speed (bytes/s)':<30}")
print("-" * 60)
print(f"{dowload_speed:<30} {upload_speed:<30}")    
