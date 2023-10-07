class ope:
    def __init__(self):
        self.p = input("Enter value:")

    def __eq__(self, other):
        if self.p == other.p:
            print("both are same:")
        else:
            print("not same:")


op1 = ope()
op2 = ope()
op1 == op2
