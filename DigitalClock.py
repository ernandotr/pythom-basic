import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

clocl_label = tk.Label(root, font=("Helvetica", 50), background="black", foreground="cyan")
clocl_label.pack(anchor="center", fill="both", expand=True)

def update_time():
    current_time = strftime("%H:%M:%S %p")
    clocl_label.config(text=current_time)
    clocl_label.after(1000, update_time)

update_time()
root.mainloop()
