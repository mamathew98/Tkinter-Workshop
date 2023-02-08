import tkinter as tk


class Window:
    def __init__(self, master):
        self.master = root

        self.frame = tk.Frame(self.master, width=200, height=200)
        self.frame.pack()

        # Create a assigned variable
        self.var = tk.StringVar()
        # Initialize value
        self.var.set('Hello World')

        # Assign label value to variable
        self.label = tk.Label(self.frame, textvariable=self.var)
        self.label.place(x=30, y=50)

        self.button = tk.Button(self.frame, text="Click Me!", command=self.command1)
        self.button.place(x=30, y=80)

    def command1(self):
        # Change the variable when button clicked
        self.var.set('Button Clicked')


root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()