import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, width=400, height=300)
        self.frame.pack()

        # Create Scale and have fun with attributes
        self.scale = tk.Scale(self.frame, from_=0, to=10, length=200, tickinterval=1, sliderlength=20)
        self.scale.place(x=30, y=30)

        self.scale2 = tk.Scale(self.frame, from_=0, to=10, orient=tk.HORIZONTAL, command=self.submit, label='Test', troughcolor='blue')
        self.scale2.place(x=90, y=30)

        self.scale3 = tk.Scale(self.frame, from_=0, to=10, command=self.submit, resolution=0.5, digit=3, showvalue=0)
        self.scale3.place(x=180, y=30)

        # Manage active and passive state
        self.button = tk.Button(self.frame, text='DISABLE SCALE', command=self.disable)
        self.button.place(x=200, y=220)

    def submit(self, value):
        print(value)

    # Disable the scale
    def disable(self):
        self.scale2.config(state=tk.DISABLED)

root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()