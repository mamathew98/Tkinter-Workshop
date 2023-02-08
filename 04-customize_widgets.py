import tkinter as tk


class Window:
    def __init__(self, master):
        self.master = root

        self.frame = tk.Frame(self.master, width=200, height=200)
        self.frame.pack()

        self.var = tk.StringVar()
        self.var.set('Hello World')

        # Change text color and font
        self.label = tk.Label(self.frame, textvariable=self.var, fg="blue", font='Verdana 14')
        self.label.place(x=30, y=50)

        # Change shape of button -> width is number of characters and height is number of lines
        self.button = tk.Button(self.frame, text="Click Me!", command=self.command1, width=10, height=2)
        self.button.place(x=30, y=80)

    def command1(self):
        self.var.set('Button Clicked')


root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()