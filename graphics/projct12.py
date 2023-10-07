from tkinter import *  
a=Tk()  
a.title("list and scrollbar")  
list1=Listbox(a,width=25,height=25,justify=CENTER,bg="pink",bd=20)  
scroll=Scrollbar(a,command=list1.yview)  
  
list1.configure(yscrollcommand=scroll.set)  
list1.pack(side=LEFT)  
scroll.pack(side=RIGHT,fill=Y)  
for q in range(500):  
    list1.insert(END,q)  




mainloop()
