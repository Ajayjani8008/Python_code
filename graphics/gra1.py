from tkinter import *
from math import *
top = Tk()
top.title("Calculater")
top.geometry("150x150")
top.resizable(1, 1)
equation = StringVar()
expression = ""


def getandreplace():
    """replace x with * and / with /"""
    expression = e.get()
    newtext = expression.replace('/', '/')
    newtext = newtext.replace('x', '*')


def clear():
    global expression
    expression = ""
    equation.set("")


def click(item):
    global expression
    expression = expression+str(item)
    equation.set(expression)


def equal():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""


expression = ""

Entry(top, textvariable=equation).grid(
    row=1, column=1, rowspan=2, columnspan=5)
Button(top, text="+", padx=10, pady=8,
       command=lambda: click('+')).grid(row=3, column=1)
Button(top, text="-", pady=10, padx=8,
       command=lambda: click('-')).grid(row=3, column=2)
Button(top, text="*", pady=10, padx=8,
       command=lambda: click('*')).grid(row=3, column=3)
Button(top, text="/", pady=10, padx=8,
       command=lambda: click('/')).grid(row=3, column=4)
Button(top, text="=", pady=10, padx=8,
       command=lambda: equal()).grid(row=4, column=1)
Button(top, text="1", pady=10, padx=8,
       command=lambda: click(1)).grid(row=4, column=2)
Button(top, text="2", pady=10, padx=8,
       command=lambda: click(2)).grid(row=4, column=3)
Button(top, text="3", pady=10, padx=8,
       command=lambda: click(3)).grid(row=4, column=4)
Button(top, text="4", pady=10, padx=8,
       command=lambda: click(4)).grid(row=5, column=1)
Button(top, text="4", pady=10, padx=8,
       command=lambda: click(4)).grid(row=5, column=1)
Button(top, text="5", pady=10, padx=8,
       command=lambda: click(5)).grid(row=5, column=2)
Button(top, text="6", pady=10, padx=8,
       command=lambda: click(6)).grid(row=5, column=3)
Button(top, text="7", pady=10, padx=8,
       command=lambda: click(7)).grid(row=5, column=4)
Button(top, text="8", pady=10, padx=8,
       command=lambda: click(8)).grid(row=6, column=1)
Button(top, text="9", pady=10, padx=8,
       command=lambda: click(9)).grid(row=6, column=2)
Button(top, text="0", pady=10, padx=8,
       command=lambda: click(0)).grid(row=6, column=3)
Button(top, text="AC", pady=10, padx=8,
       command=lambda: clear()).grid(row=6, column=3)


top.mainloop()
