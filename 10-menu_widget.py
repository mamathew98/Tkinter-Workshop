import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, width=400, height=300)
        self.frame.pack()

        # Create menu button
        self.mbutton = tk.Menubutton(self.frame, text='Menu Button', relief=tk.RAISED)

        # Create Menu
        self.menu = tk.Menu(self.mbutton, tearoff=0)
        self.menu.add_command(label='Load', command=self.command1)
        self.menu.add_command(label='Save', command=self.command1)

        # Add Check Button
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.menu.add_checkbutton(label='Check1', variable=self.var1, command=self.command2)
        self.menu.add_checkbutton(label='Check2', variable=self.var2, command=self.command2)

        self.mbutton['menu'] = self.menu

        self.mbutton.place(x=30, y=50)


    def command1(self):
        print('Menu Clicked')
    def command2(self):
        print(self.var1.get())
        print(self.var2.get())
    def submit(self, value):
        print(value)


root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()