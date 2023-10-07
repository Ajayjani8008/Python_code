from tkinter import*


parent = Tk()

Lb1 = Listbox(parent)
Lb1.insert(1, "18")
Lb1.insert(2, "19")
Lb1.insert(3, "20")
Lb1.insert(4, "21")
Lb1.insert(5, "22")
Lb1.insert(6, "21")

Lb1.pack()


parent.mainloop()