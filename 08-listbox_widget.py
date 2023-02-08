import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, width=400, height=300)
        self.frame.pack()

        # Label for list
        self.label = tk.Label(self.frame, text="This is a List")
        self.label.place(x=30, y=20)

        # Create Listbox
        self.listbox = tk.Listbox(self.frame, selectmode='multiple', height=5)
        self.listbox.insert(0, 'Meat')
        self.listbox.insert(1, 'Milk')
        self.listbox.insert(2, 'Eggs')
        self.listbox.insert(3, 'Cheese')
        self.listbox.place(x=30, y=50)

        # Retrieve Selection
        self.button = tk.Button(self.frame, text='Submit', command=self.submit)
        self.button.place(x=200, y=220)

    def submit(self):
        # Return index of selected 
        print(self.listbox.curselection())
        # Return All Values
        print(self.listbox.get(0, tk.END))

root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()