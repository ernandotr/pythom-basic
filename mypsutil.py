import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

print(f"Battery is at {percent}%")
if plugged:
    print("The device is plugged in.")