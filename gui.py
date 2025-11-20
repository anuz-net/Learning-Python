from tkinter import *

root = Tk()

mylabel1 = Label(root, text="Hello World")
mylabel2 = Label(root, text = "Yay")
mylabel1.pack()
mylabel2.pack()

def myclick():
    lbl = Label(root, text="Look I Create a Buttn")


root.mainloop()