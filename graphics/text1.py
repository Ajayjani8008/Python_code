from tkinter import*
top=Tk()
text=Text(top)
text.insert(INSERT, "Name.....")  
text.insert(END, "Salary.....")  
text.pack()
text.tag_add("Write Hare","1.0","1.4")
text.tag_add("Click Hare","1.8","1.13")


text.tag_config("Write Here",background="yellow",foreground="black")
text.tag_config("Click Here",background="red",foreground="white")
top.mainloop()
