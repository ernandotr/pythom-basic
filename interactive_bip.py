import os
import time 
import tkinter as tk

# os.system("beep -f 1000 -l 500")

os.system("afplay /System/Library/Sounds/Ping.aiff")
time.sleep(1)

os.system("afplay /System/Library/Sounds/Glass.aiff")

window = tk.Tk()
window.title("Interactive Beep")
window.geometry("300x200")
def play_beep():
    os.system("afplay /System/Library/Sounds/Ping.aiff")
button = tk.Button(window, text="Play Beep", command=play_beep)
button.pack(pady=50)
window.mainloop()
