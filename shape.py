class shape:
    pass


class circle(shape):
    def input(self):
        circle.redius = int(input("Enter The Redius of CIrcle: "))

    def display(self):
        circle.area = (3.14)*(circle.redius)*(circle.redius)
        print("AREA of the circle is :", circle.area)


class reactengle(shape):
    def input(self):
        reactengle.length = int(input("Enter The Length of reactangle: "))
        reactengle.wedgth = int(input("Enter The wedgth of reactangle: "))

    def display(self):
        reactengle.area = (reactengle.length)*(reactengle.wedgth)
        print("AREA of the reactangle is :", reactengle.area)


class square(shape):
    def input(self):
        square.length = int(input("Enter The Length of square: "))

    def display(self):
        square.area = (square.length)*(square.length)
        print("AREA of the reactangle is :", square.area)


c = circle()
c.input()
c.display()
r = reactengle()
r.input()
r.display()
s = square()
s.input()
s.display()
