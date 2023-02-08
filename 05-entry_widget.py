import tkinter as tk


class Window:
    def __init__(self, master):
        # This Should be equal Master
        self.master = master

        self.frame = tk.Frame(self.master, width=300, height=200)
        self.frame.pack()

        # Create labels for entries
        self.label = tk.Label(self.frame, text='Username')
        self.label.place(x=30, y=50)
        self.label = tk.Label(self.frame, text='Password')
        self.label.place(x=30, y=80)

        # Create & Customize Entries
        self.entry = tk.Entry(self.frame, width=20, bd=4)
        # Insert text in entry as placeholder
        self.entry.insert(0, "Username")
        self.entry.place(x=100, y=50)

        # Hide entered password
        self.entry2 = tk.Entry(self.frame, width=20, bd=4, show="*")
        # Insert text in entry as placeholder
        self.entry2.insert(0, "Psasword")
        self.entry2.place(x=100, y=80)

        # Create submit button
        self.button = tk.Button(self.frame, text="Submit", command=self.submit)
        self.button.place(x=150, y=120)

    def submit(self):
        # Get entry data
        print(self.entry.get())
        print(self.entry2.get())

root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()