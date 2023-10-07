class Product:
    def input(self):
        self.p_code = int(input("enter product code:"))
        self.p_name = input("enter product name:")
        self.p_qty = int(input("enter product qty:"))


class stock(Product):
    def update(self):
        print(self.p_qty, self.p_name, self.p_code)


class sales(stock):
    def sell_pro(self):
        self.sell = int(input("enter  the sold amount:"))
        self.p_qty = (self.p_qty)-(self.sell)


class purchase(stock):
    def purchase_pro(self):
        self.pur = int(input("enter the purvhase amount"))
        self.p_qty = self.p_qty+self.pur


s1 = sales()
s1.input()
s1.sell_pro()
s1.update()

p1 = purchase()
p1.input()
p1.purchase_pro()
p1.update()
