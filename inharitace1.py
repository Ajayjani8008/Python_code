class Product:
    def input(self):
        pass


class wholesaler(Product):
    def input1(self):
        wholesaler.w_qty = int(
            input("enter quntity of the wholesaler's  product:"))
        wholesaler.w_price = int(input("enter wholesaler's price:"))

    def display1(self):
        print("""the datais of  the  wholesaler's  product is ..""", wholesaler.w_qty)
        print("""price of the product for wholesaler is:""", wholesaler.w_price)


class retailer(Product):
    def input2(self):
        retailer.r_qty = int(
            input("enter quntity of the retailer's  product:"))
        retailer.r_price = int(input("enter retailer's price:"))

    def display2(self):
        print('''quntity of product for retailer  is ..''', retailer.r_qty)
        print("""price of product for retaler is :""", retailer.r_price)


class sale(wholesaler, retailer):
    def display(self):
        sale.total_sale = wholesaler.w_qty+retailer.r_qty
        sale.total_amt1 = retailer.r_qty*retailer.r_price
        sale.total_amt2 = wholesaler.w_qty*wholesaler.w_price
        sale.profit = sale.total_amt1-sale.total_amt2
        print("toral sale :", sale.total_sale)
        print("the retailer amount is:", sale.total_amt1)
        print("the wholesaler amount is:", sale.total_amt2)
        print("total profit is:", sale.profit)


s1 = sale()
s1.input1()
s1.display1()
s1.input2()
s1.display2()
s1.input()
s1.display()
