import psutil

print(f"{'PID':<10} {'Name':<25} {'Status':<15} {'Memory%':<10} {'CPU%':<10} { 'User':<20}")
print("-" * 90)
for proc in psutil.process_iter(['pid', 'name', 'status', 'memory_percent', 'cpu_percent', 'username']):
    try:
        pid = proc.info['pid']
        name = proc.info['name'][:24]  # Truncate to fit
        status = proc.info['status']
        memory_percent = f"{proc.info['memory_percent']}"
        if(memory_percent != 'None'):
            memory_percentFloat = float(memory_percent)
            memory_percentRounded = f"{memory_percentFloat:.3f}"

            cpu_percent = f"{proc.info['cpu_percent']}"
            username = proc.info['username'][:19]  # Truncate to fit

            print(f"{pid:<10} {name:<25} {status:<15} {memory_percentRounded:<10} {cpu_percent:<10} {username:<20}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass