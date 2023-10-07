from tkinter import*
ttt=Tk()
ttt.geometry("")
def select():
    sel="value=.."+str(v.get())
    label.config(text=sel)

v=IntVar()
scale=Scale(ttt,variable=v,from_=1,to=50,orient=HORIZONTAL)
scale.pack(anchor=CENTER)
btn=Button(ttt,text="Value",command=select)
btn.pack(anchor=CENTER)
label=Label(ttt)
label.pack()



ttt.mainloop()
