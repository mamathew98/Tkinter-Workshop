import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, width=300, height=200)
        self.frame.pack()

        # Create Combobox
        # First we need to create list of options
        self.vlist=[
            "Option1",
            "Option2",
            "Option3",
            "Option4",
            "Option5",
            "Option6",
            "Option7",
            "Option8",
            "Option9",
        ]

        self.combo = ttk.Combobox(self.frame, values=self.vlist, height=5)
        self.combo.place(x=30, y=30)
        # Readonly comboboxes can't be edited
        self.combo2 = ttk.Combobox(self.frame, values=self.vlist, state='readonly', justify='center', height=5)
        # Give it some default option
        self.combo2.set("Option1")
        self.combo2.place(x=30, y=60)


        # Retrieve Selection
        self.button = tk.Button(self.frame, text='Click Me!', command=self.submit)
        self.button.place(x=30, y=100)

    def submit(self):
        print(self.combo.get())
        print(self.combo2.get())
        

root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()