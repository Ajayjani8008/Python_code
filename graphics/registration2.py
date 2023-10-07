from tkinter import*

from math import *
import mysql.connector



top=Tk()
top.title("student detais")
# top.geometry("500x345")
equation1=StringVar()
equation2=StringVar()
equation3=StringVar()
equation4=StringVar()
equation5=StringVar()
equation6=StringVar()
equation7=StringVar()
equation8=StringVar()
equation9=StringVar()
equation10=StringVar()
equation11=StringVar()



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

mycon=mysql.connector.connect(host='localhost',user='root',passwd = "",database='regestration')
cur = mycon.cursor()

def sub():

    for i in btn1.curselection():
        print(btn1.get(i))
        print(e1.get(),e2.get(),e3.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get())



        try:
            cur.execute("insert into reg(Name,Address,Age,ContactNo,10thPD,10thSch,12thPD,12thSch,PanCardNo,AadharCard,Voterid) values('"+ e1.get() +"','"+ e2.get() +"','"+btn1.get(i)+"','"+ e3.get() +"','"+ e5.get() +"','"+ e6.get() +"','"+ e7.get() +"','"+ e8.get() +"','"+ e9.get() +"','"+ e10.get() +"','"+ e11.get()+ "')")
            
            mycon.commit()

        except:
            mycon.rollback() 

def update():

    try:
        cur.execute("Update reg set ContactNo='"+ e3.get() +"' where Name='"+ e1.get() +"' ")
        mycon.commit()

    except:
        mycon.rollback() 

def delete():

    try:
        cur.execute("delete from reg  where Name='"+ e1.get() +"' ")
        mycon.commit()

    except:
        mycon.rollback() 

def select():

    try:
        cur.execute("select * from reg ")
        abc=cur.fetchall()
        print(abc)
        mycon.commit()

    except:
        mycon.rollback() 



PD=Label(top,text="--------Personal data--------",font=('arial',15,'bold')).grid(row=0,column=1)



name=Label(top,text="Name",font=('arial',12,'bold')).grid(row=1,column=0)
e1=Entry(top,textvariable=equation1)
e1.grid(row=1,column=1)

Address=Label(top,text="Address",font=('arial',12,'bold')).grid(row=2,column=0)

e2=Entry(top,textvariable=equation2)
e2.grid(row=2,column=1)

ContactNo=Label(top,text="ContactNo",font=('arial',12,'bold')).grid(row=3,column=0)
e3=Entry(top,textvariable=equation3)
e3.grid(row=3,column=1)

Age=Label(top,text="Age",font=('arial',12,'bold')).grid(row=4,column=0)
# e4=Entry(top,textvariable=equation4)
btn1=Listbox(top,selectmode=MULTIPLE)
btn1.grid(row=4,column=1)
btn1.insert(1,"18")
btn1.insert(2,"19")
btn1.insert(3,"20")
btn1.insert(4,"21")
btn1.insert(5,"22")
btn1.insert(6,"23")
btn1.insert(7,"24")
btn1.insert(8,"25")
btn1.insert(9,"26")
btn1.insert(10,"27")
btn1.insert(11,"28")



ED=Label(top,text="---------Educational data------",font=('arial',15,'bold')).grid(row=5,column=1)

M1=Label(top,text="10th PD ",font=('arial',12,'bold')).grid(row=6,column=0)
e5=Entry(top,textvariable=equation5)
e5.grid(row=6,column=1)

M2=Label(top,text="10th Sch",font=('arial',12,'bold')).grid(row=7,column=0)
e6=Entry(top,textvariable=equation6)
e6.grid(row=7,column=1)

M3=Label(top,text="12th PD",font=('arial',12,'bold')).grid(row=8,column=0)
e7=Entry(top,textvariable=equation7)
e7.grid(row=8,column=1)

M4=Label(top,text="12th Sch",font=('arial',12,'bold')).grid(row=9,column=0)
e8=Entry(top,textvariable=equation8)
e8.grid(row=9,column=1)



AC=Label(top,text="---------All Card Details------",font=('arial',15,'bold')).grid(row=10,column=1)

A1=Label(top,text="Pan Card No: ",font=('arial',12,'bold')).grid(row=11,column=0)
e9=Entry(top,textvariable=equation9)
e9.grid(row=11,column=1)

A2=Label(top,text="Aadhar Card:",font=('arial',12,'bold')).grid(row=12,column=0)
e10=Entry(top,textvariable=equation10)
e10.grid(row=12,column=1)

M3=Label(top,text="Voter id:",font=('arial',12,'bold')).grid(row=13,column=0)
e11=Entry(top,textvariable=equation11)
e11.grid(row=13,column=1)



b=Button(top,text="SUBMIT",bg="Black",fg="White",command=sub).grid(row=15,column=0)
b1=Button(top,text="REST",bg="Black",fg="White",command=lambda:clear()).grid(row=15,column=3)
b2=Button(top,text="UPDATE",bg="Black",fg="White",command=lambda:update()).grid(row=15,column=2)
b3=Button(top,text="DELETE",bg="Black",fg="White",command=lambda:delete()).grid(row=15,column=1)
b4=Button(top,text="SELECT",bg="Black",fg="White",command=lambda:select()).grid(row=15,column=4)





top.mainloop()



