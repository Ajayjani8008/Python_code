from tkinter import*
def donothig():
    filewin=Toplevel(root)
    button=Button(filewin,text="Do nothing  button")
    button.pack()
root=Tk()
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=donothig)
filemenu.add_command(label="open",command=donothig)
filemenu.add_command(label="save",command=donothig)
filemenu.add_command(label="Save As..",command=donothig)
filemenu.add_command(label="Close",command=donothig)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",command=donothig)
editmenu.add_command(label="Cut",command=donothig)
editmenu.add_command(label="Peste", command=donothig)
editmenu.add_command(label="Delete", command=donothig)
editmenu.add_command(label="Select All", command=donothig)
menubar.add_cascade(label="Edit", menu=editmenu)

formatemanu=Menu(menubar,tearoff=0)
formatemanu.add_command(label="Word wrap",command=donothig)
formatemanu.add_command(label="...Font",command=donothig)
menubar.add_cascade(label="Formate",menu=formatemanu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothig)
helpmenu.add_command(label="About...", command=donothig)
menubar.add_cascade(label="Help", menu=helpmenu)


viewmenu=Menu(menubar,tearoff=0)
viewmenu.add_command(label="Zoom in",command=donothig)
viewmenu.add_command(label="",command=donothig)
viewmenu.add_command(label="",command=donothig)
viewmenu.add_command(label="",command=donothig)
menubar.add_cascade(label="view",menu=viewmenu)


root.config(menu=menubar)
root.mainloop()






























































