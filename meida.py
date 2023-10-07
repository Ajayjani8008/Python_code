class Media:
    def __init__(self):
        Media.title = input("Enter the title of the divice:")
        Media.price = int(input("Eenter the price of the divice:"))
    def disply(self):
        print("title of the divice ...>>>>", Media.title)
        print("price of the divice ...>>>>", Media.price)
class Harddisk(Media):
    def input1(self):
        Harddisk.hdd_type = input("Enter the type of the  harddisk:")
        Harddisk.qty = input("Enter the quntity of the  harddisk:")
    def disply1(self):
        print("type of the harddisk ....>>>", Harddisk.hdd_type)
        print("quntity of the harddisk ....>>>", Harddisk.qty)
class Pendrive(Media):
    def input2(self):
        Pendrive.pendrive_type = input("Enter the type of the pendrive:")
        Pendrive.qty = input("Enter the quantity of the pendrive:")
    def disply2(self):
        print("type of the Pendrive ....>>>", Pendrive.pendrive_type)
        print("quntity of the Pendrive ....>>>", Pendrive.qty)
h=Harddisk()
h.input1()
h.disply1()
h.disply()
p=Pendrive()
p.input2()
p.disply2()
