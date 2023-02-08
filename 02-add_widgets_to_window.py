import tkinter as tk


class Window:
    def __init__(self, master):
        self.master = root

        # Create a Frame
        self.frame = tk.Frame(self.master, width=200, height=200)
        # Position the element
        self.frame.pack()

        # Create a Label
        self.label = tk.Label(self.frame, text='Hello World!')
        # Place the element
        self.label.place(x=30, y=50)

        # Create a Button and give it functionality
        self.button = tk.Button(self.frame, text="Click Me!", command=self.command1)
        # Place the elemen
        self.button.place(x=30, y=80)

    # Button function
    def command1(self):
        print('Button has been clicked')


root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()