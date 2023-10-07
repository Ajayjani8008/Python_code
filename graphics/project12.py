from tkinter import *
from tkinter import messagebox


def sum():
    sum = 0
    num = e1.get()
    for i in range(1, int(num)+1):

        sum = sum+i
        l1.config(text=str(sum))


root = Tk()
label = Label(root, text="Enter the one number:")
label.pack()
e1 = Entry(root)
e1.pack()
btn = Button(root, text="meracle", command=sum)
btn.pack()
l1 = Label(root)
l1.pack()
root.mainloop()
