from tkinter import*
from PIL import Image,ImageTk
ajay=Tk()
ajay.geometry("565x576")
jay=Image.open("MSdhoni.jpg")
photo=ImageTk.PhotoImage(jay)
ajay_lable= Label(image=photo)
ajay_lable.pack()



# photo=PhotoImage(file="123.png")

# mylable=Label(image=photo)
# mylable.pack()
ajay.mainloop()