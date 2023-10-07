
from tkinter import *  
  
top = Tk()  
top.geometry("100x100")  
  
labelframe1 = LabelFrame(top, text=" my name")  
labelframe1.pack(fill="both", expand="yes")  
  
toplabel = Label(labelframe1, text="say ajay jani")  
toplabel.pack()  
  
labelframe2 = LabelFrame(top, text = "my wish",background="red")  
labelframe2.pack(fill="both", expand = "yes")  
  
bottomlabel = Label(labelframe2,text = "no wish  take place")  
bottomlabel.pack()  
  
top.mainloop()  