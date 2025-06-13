import tkinter as tk

root = tk.Tk()

print(tk.TkVersion)
print(tk.TclVersion)

label = tk.Label(root, text="Hello, Tkinter!", fg="yellow", font=("Arial", 16))
label.pack(padx=20, pady=20)

root.mainloop()
