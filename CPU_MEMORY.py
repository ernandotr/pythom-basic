import tkinter as tk, psutil

root = tk.Tk()
root.title("CPU and Memory Usage")
root.geometry("300x150")
root.configure(bg="black")

lbl = tk.Label(root, font=("Helvetica", 16), bg="black", fg="lime")
lbl.pack(expand=True)

def update_usage():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    battery = psutil.sensors_battery()
    lbl.config(text=f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory}%\nBattery: {battery.percent}%")
    root.after(1000, update_usage)

update_usage()
root.mainloop()

