from tkinter import *
from math import *
parent = Tk()
equation1 = StringVar()
equation2 = StringVar()
equation3 = StringVar()
equation4 = StringVar()
equation5 = StringVar()
equation6 = StringVar()
equation7 = StringVar()
equation8 = StringVar()
equation9 = StringVar()
equation10 = StringVar()
equation11 = StringVar()
equation12 = StringVar()


def clear():
    equation1.set("")
    equation2.set("")
    equation3.set("")
    equation4.set("")
    equation5.set("")
    equation6.set("")
    equation7.set("")
    equation8.set("")
    equation9.set("")
    equation10.set("")
    equation11.set("")
    equation12.set("")


parent.title("Student Registrstion Form.........")
Hadding = Label(parent, text="---------------------------------PERSONAL DETAILS------------------------------",
                font=('arial', 18, 'bold')).grid(row=0, column=7)
name = Label(parent, text="Name").grid(row=1, column=0)
e1 = Entry(parent, textvariable=equation1).grid(row=1, column=1)
Address = Label(parent, text="Address").grid(row=2, column=0)
e2 = Entry(parent, textvariable=equation2).grid(row=2, column=1)
Contact_number = Label(parent, text="Contact Number").grid(row=3, column=0)
e3 = Entry(parent, textvariable=equation3).grid(row=3, column=1)
Age = Label(parent, text="Age").grid(row=4, column=0)


Lb1 = Listbox(parent,MULTIPLE)

Lb1.insert(1, "18")
Lb1.insert(2, "19")
Lb1.insert(3, "20")
Lb1.insert(4, "21")
Lb1.insert(5, "22")
Lb1.insert(7, "23")
Lb1.insert(8, "24")
Lb1.insert(9, "25")
Lb1.insert(10, "26")
Lb1.insert(11, "27")
Lb1.insert(12, "28")
Lb1.insert(13, "29")
Lb1.insert(14, "30")
Lb1.grid(row=4,column=1)





# e4 = Entry(parent, textvariable=equation4).grid(row=4, column=1)
date_of_birth = Label(parent, text="Date Of Birth").grid(row=5, column=0)
e5 = Entry(parent, textvariable=equation5).grid(row=5, column=1)
Hadding2 = Label(parent, text="---------------------------------EDUCATION  DETAILS------------------------------",
                 font=('arial', 18, 'bold')).grid(row=8, column=7)
Pm10 = Label(parent, text="10th Passing Marks").grid(row=10, column=0)
e6 = Entry(parent, textvariable=equation6).grid(row=10, column=1)
Ps10 = Label(parent, text="10th Passing School").grid(row=11, column=0)
e8 = Entry(parent, textvariable=equation7).grid(row=11, column=1)
Pm12 = Label(parent, text="12th Passing Marks").grid(row=12, column=0)
e0 = Entry(parent, textvariable=equation8).grid(row=12, column=1)
Ps12 = Label(parent, text="12th Passing School").grid(row=13, column=0)
e9 = Entry(parent, textvariable=equation9).grid(row=13, column=1)
Hadding3 = Label(parent, text="---------------------------------ALL CARD NUMBERS------------------------------",
                 font=('arial', 18, 'bold')).grid(row=14, column=7)
ac = Label(parent, text="Adhar Card Number").grid(row=15, column=0)
c1 = Entry(parent, textvariable=equation10).grid(row=15, column=1)
pn = Label(parent, text="PAN Card Number").grid(row=16, column=0)
c2 = Entry(parent, textvariable=equation11).grid(row=16, column=1)
vn = Label(parent, text="Voterid Card Number").grid(row=17, column=0)
c3 = Entry(parent, textvariable=equation12).grid(row=17, column=1)
Button(parent, text="Submit", pady=10, padx=8).grid(row=19, column=7)
Button(parent, text="Reset", command=lambda: clear(),
       pady=10, padx=8).grid(row=19, column=8)






parent.mainloop()
