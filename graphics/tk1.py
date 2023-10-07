from tkinter import*



root=Tk()
root.geometry("1000x1000")
w=Canvas(root,background="red",height=200,scrollregion=(0,0,10000,10000))
l=Label(root,text="myname",highlightbackground="blue",relief=SUNKEN,height=10,width=150)
i1=w.create_line(0,0,500,600,width=5,fill="blue")
i2=w.create_line(0,600,500,0,width=5,fill="grey")
i3=w.create_oval(0,600,500,0,width=7,fill="grey")
i4=w.create_arc(1000,30,500,600,width=7,fill="white",start=0,extent=100,)
l.pack()
w.pack()


root.mainloop()
