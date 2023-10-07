from tkinter import*
top=Tk()
top.geometry("")
# spin=Spinbox(top,from_=-1,to=34)
# spin.pack()


def add():
    a=(e1.get())
    b=(e2.get())
    leftdata=str(a+b)
    left.insert(3,leftdata)
    

w1=PanedWindow()
w1.pack(fill=BOTH,expand=1)
left=Entry(w1,bd=20)
w1.add(left)
w2 = PanedWindow(w1, orient = VERTICAL)  
w1.add(w2)  


e1 = Entry(w2)  
e2 = Entry(w2)  


w2.add(e1)
w2.add(e2)

b1=Button(w2,text="add",command=add)
w2.add(b1)




top.mainloop()
