from tkinter import *
from spamClassifier import *
from spamClassifier import *

root = Tk()
root.title("SPAM-CLASSIFIER")
root.iconbitmap("PSYCODER Logo.png")

e = Entry(root, width=50, bg="yellow", fg="black", borderwidth=5)
e.pack()
e.insert(0, "Enter your Message")


# mylabel1 = Label(root, text="SPAM-CLASSIFIER")
# mylabel2 = Label(root, text="PSYCODER")
# mylabel3 = Label(root, text="Text the message:")
# mylabel1.pack()
# mylabel2.pack()
# mylabel3.pack()

def myClick():
    mylabel4 = Label(root, text=message(e.get()))
    mylabel4.pack()


def mydelete():
    e.delete(0, END)


mybutton1 = Button(root, text="Click Me", padx=20, pady=5, command=myClick, fg="yellow", bg="black",)
mybutton1.pack()

mybutton2 = Button(root, text="CLEAR", padx=20, pady=5, command=mydelete, fg="red", bg="black")
mybutton2.pack()

root.mainloop()
