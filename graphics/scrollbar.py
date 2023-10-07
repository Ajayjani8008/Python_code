from tkinter import*
tom=Tk()

SB=Scrollbar(tom)
SB.pack(side=RIGHT,fill=Y)
mylist=Listbox(tom,yscrollcommand=SB.set)
for line in range(30):
    mylist.insert(END,"Number"+str(line))
mylist.pack(side=LEFT)
SB.config(command=mylist.yview)








tom.mainloop()

