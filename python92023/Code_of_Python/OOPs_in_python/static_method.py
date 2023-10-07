class maths:
    def __init__(self,num):
        self.num=num

    def add(self,n):
        self.num=self.num+n

    @staticmethod
    def ajay(a,b):#there is no Mandatory  or compulsary use self keyword
        return a+b
a=maths(10)
print(a.num)
a.add(30)
print(a.num)
print(a.ajay(5,6))
print(maths.ajay(7,88)) #we can  call methad  by adding class name 
