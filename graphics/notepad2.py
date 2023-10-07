import re
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog, simpledialog
from tkinter.scrolledtext import ScrolledText
root = Tk()
root.title("DataFlair NotePad")
root.resizable(0, 0)
notepad = ScrolledText(root, width=100, height=40)
fileName = ''


def cmdNew():  # file menu new option
    global fileName
    if len(notepad.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Notepad", "Do you wnat to save changes?"):
            cmdsave()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")


def cmdOpen():
    fd = filedialog.askopenfile(parent=root, mode='r')
    t = fd.read()
    notepad.insert(0, 0, t)


def cmdsave():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd != None:
        data = notepad.get("1.0", END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")


def cmdSaveAs():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = notepad.get(0.0, END)

    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message="Not able to save file!")


def cmdExit():
    if messagebox.askyesno("Notepad", "Are you sure you want to exit?"):
        root.destroy()


def cmdCut():
    notepad.event_generate("<<Cut>>")


def cmdCopy():
    notepad.event_generate("<<Copy>>")


def cmdPaste():
    notepad.event_generate("<<Paste>>")


def cmdClear():
    notepad.event_generate("<<Clear>>")


def cmdFind():
    notepad.tag_remove("Found", '1.0', END)
    find = simpledialog.askstring("Find", "Find what:")
    if find:
        idx = '1.0'
    while 1:
        idx = notepad.search(find, idx, nocase=1, stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' % (idx, len(find))
        notepad.tag_add('found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('found', foreground='white', background='blue')
    notepad.bind("<1>", click)


def click(event):
    notepad.tag_config('Found', background="white", foreground="black")


def cmdSelectAll():  
    notepad.event_generate("<<SelectAll>>")


def cmdTimeDate(): 
    now = datetime.now()
  
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("About Notepad", "Notepad by -\nDataFlair")
def cmdAbout():  
    label = messagebox.showinfo("About Notepad", "Notepad by - \nDataFlair")



notepadMenu = Menu(root)
root.configure(menu=notepadMenu)
fileMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=cmdNew)
fileMenu.add_command(label='Open', command=cmdOpen)
fileMenu.add_command(label='Save', command=cmdsave)
fileMenu.add_command(label='Save As...', command=cmdSaveAs)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=cmdExit)
editMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='Edit', menu = editMenu) 
editMenu.add_command(label='Cut', command=cmdCut)
editMenu.add_command(label='Copy', command=cmdCopy)
editMenu.add_command(label='Paste', command=cmdPaste)
editMenu.add_command(label='Delete', command=cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Find...', command=cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Select All', command=cmdSelectAll)
editMenu.add_command(label='Time/Date', command=cmdTimeDate)

helpMenu = Menu(notepadMenu, tearoff=False)
notepadMenu.add_cascade(label='Help', menu=helpMenu)

helpMenu.add_command(label='About Notepad', command=cmdAbout)
notepad.pack()
root.mainloop()
