from tkinter import*

root=Tk()


l2=Listbox(root,width=15,height=100,justify=CENTER,font=30,bg="grey",bd=20)
l3=Listbox(root,width=15,height=100,justify=LEFT,font=30,bg="red",bd=20)
scroll=Scrollbar(root,command=l2.yview) 
scroll=Scrollbar(root,command=l3.yview) 
l2.configure(yscrollcommand=scroll.set)
l3.configure(yscrollcommand=scroll.set)
l2.pack(side=LEFT)
l3.pack(side=RIGHT)
scroll.pack(side=RIGHT,fill=Y) 
scroll.pack(side=RIGHT,fill=Y)
for q in range(100):  
    l2.insert(END,q) 
for q in range(100):  
    l3.insert(END,q) 




root.mainloop()

