from tkinter import *
from tkinter import messagebox
import math

import random
root = Tk()
plyer1 = 0
plyer2 = 0
equation1 = 0


def calculate():
    global equation1
    global plyer1
    global plyer2
    equation1 = random.randint(0, 10)
    l3.config(text=equation1)
    print(equation1)
    if int(e1.get())>int(equation1):
        plyer1=plyer1+1
        l4.config(text=plyer1)
        # l5.config(text=plyer2)
    elif int(e1.get())<int(equation1):
        plyer2=plyer2+1
        # l4.config(text=plyer1)
        l5.config(text=plyer2)


def reset():
    pass

    

def winner():
    if plyer1>plyer2:
        l6.config(text="winner winner chicken dinner")
    else:
                l6.config(text="batter luck , next time...............")


input1 = Label(root, text="Enter your Number",
               font="bold").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)



# input2=Label(root,text="Genreted Number",font="bold").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)

b1 = Button(root, text="Calculate", foreground="red",
            font="bold", command=calculate).grid(row=3, column=0)
b2 = Button(root, text="Reset", foreground="red", font="bold",
            command=lambda: reset).grid(row=3, column=1)
b3 = Button(root, text="winner", foreground="red",
            font="bold", command=winner).grid(row=3, column=2)

output1 = Label(root, text="Your points is:",
                font="bold").grid(row=5, column=0)
output2 = Label(root, text="Oponant points is:",
                font="bold").grid(row=6, column=0)
l3 = Label(root)
l3.grid(row=7, column=0)
l4= Label(root)
l4.grid(row=5, column=1)
l5= Label(root)
l5.grid(row=6, column=1)
l6= Label(root,bg="pink")
l6.grid(row=7, column=1)


root.mainloop()
