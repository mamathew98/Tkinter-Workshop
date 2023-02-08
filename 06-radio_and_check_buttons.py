import tkinter as tk


class Window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master, width=300, height=200)
        self.frame.pack()

        # Create radio button
        # Radio button needs variable to store
        self.var1 = tk.IntVar()

        # Radio button values should be unique
        self.radio = tk.Radiobutton(self.frame, variable=self.var1, value=1, text='Option1')
        self.radio.place(x=30, y=30)

        # Can assign command directly onto radio button
        self.radio2 = tk.Radiobutton(self.frame, variable=self.var1, value=2, text='Option2', command=self.submit)
        self.radio2.place(x=30, y=60)

        self.radio3 = tk.Radiobutton(self.frame, variable=self.var1, value=3, text='Option3')
        self.radio3.place(x=30, y=90)

        # Retrieve the value
        self.button = tk.Button(self.frame, text='Submit', command=self.submit)
        self.button.place(x=30, y=120)

    def submit(self):
        if self.var1.get() == 1: 
            print('Option 1 Selected')
        elif self.var1.get() == 2: 
            print('Option 2 Selected')
        elif self.var1.get() == 3: 
            print('Option 3 Selected')


root = tk.Tk()
root.title('Tkinter Tutorial')

window = Window(root)

root.mainloop()