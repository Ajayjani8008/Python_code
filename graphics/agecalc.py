from tkinter import*
from PIL import ImageTk,Image
from datetime import date
today=date.today()


def Age():
    # Year=2023-int(e2.get())
    # month=12-int(e3.get())
    # Day=365-int(e4.get())
  
    # l1.config(text=(str(Day)+str(-month)+str(-Day)))
 
    d= int(e4.get())
    m=int(e3.get())
    y=int(e2.get())
    age=today.year-y-((today.month, today.day)<(m,d))
    l1.config(text=str(age))
    # l1.config(state='normal')
    # l1.delete('1.0', Tk.END)
    # l1.insert(Tk.END,age)
    # l1.config(state='disabled')


pi=Tk()

img=ImageTk.PhotoImage(Image.open("D:\\Ajaykumar\\graphics\\bd_share.jpg"))
label=Label(pi,image=img)
label.pack()




label1=Label(pi,text="Name",background="blue",font=50)
label1.pack()
e1=Entry(pi)
e1.pack()

label2=Label(pi,text="Year",background="blue",font=50)
label2.pack()
e2=Entry(pi)
e2.pack()


label3=Label(pi,text="Month",background="blue",font=50)
label3.pack()
e3=Entry(pi)
e3.pack()
label4=Label(pi,text="Day",background="blue",font=50)
label4.pack()
e4=Entry(pi)
e4.pack()





btn=Button(pi,text="Calculate Your Age",command=Age)
btn.pack()

l1=Label(pi,text="Your Age is")
l1.pack()


pi.mainloop()