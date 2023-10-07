from tkinter import *
root = Tk()


def clear():
    namevalue.set("")
    phonevalue.set("")
    gendervalue.set("")
    emergancyvalue.set("")
    paymentmodevalue.set("")
    foodservicevalue.set("NULL")
 


def getvals():
    
    print("Submiting Form")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergancyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}")
    with open("Record.txt", "a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergancyvalue.get(),paymentmodevalue.get(),foodservicevalue.get()}\n")


root.geometry("")
# Heading
Label(root, text="Welcome to GDP Travels",
      font="comicsansms 13 bold", pady=15).grid(row=0, column=3)
# Text for our from
name = Label(root, text="Name", font="comicsansms 13 bold")
phone = Label(root, text="Phone", font="comicsansms 13 bold")
Gender = Label(root, text="Gender", font="comicsansms 13 bold")
emergancy = Label(root, text="Emergency Contact", font="comicsansms 13 bold")
paymentmode = Label(root, text="Payment Mode", font="comicsansms 13 bold")
# packing  text for our form
name.grid(row=1, column=2,)
phone.grid(row=2, column=2)
Gender.grid(row=3, column=2)
emergancy.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)


# tkinter varible for storing data
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergancyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergancyentry = Entry(root, textvariable=emergancyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)


# packing the entries

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergancyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# checkbox & packing it
foodservice = Checkbutton(
    root, text="Want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button & Packing  it and assigning  it a command

Button(text="Submit to GDP Travels", command=getvals).grid(row=8, column=1)
Button(text="Clear and New Entry", command=clear).grid(row=8, column=2)


root.mainloop()
