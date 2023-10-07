from tkinter import *
per = Tk()
per.geometry("")
# c=Canvas(per,height=400,bg="blue",highlightcolor="red")
# arc=c.create_arc((10,60,300,300),start=0,extent=300,fill="pink")
# c.pack()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
CB1 = Checkbutton(per, text="you are not robot.", variable=v1, onvalue=1, offvalue=0, height=10,
                  width=20, highlightcolor="red", activebackground="red", activeforeground="blue")
CB2 = Checkbutton(per, text="if you are khow pyhon.", variable=v2, onvalue=1,
                  offvalue=2, height=10, width=20, activebackground="red", activeforeground="blue")
CB3 = Checkbutton(per, text="if you are khow java script.", variable=v3, onvalue=1,
                  offvalue=2, height=10, width=20, activebackground="red", activeforeground="blue")
CB1.pack()
CB2.pack()
CB3.pack()

per.mainloop()
