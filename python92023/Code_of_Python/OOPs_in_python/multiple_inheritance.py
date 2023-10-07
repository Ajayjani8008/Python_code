'''class bycicle:
    def from_bycicle(self):
        print("i am a bycicle")
class bike:
    def from_bike(self):
        print("i am a bike")
class motorcycle:
    def from_motorcycle(self):
        print("i am motorcycle")
class vahicle(bycicle,motorcycle,bike):
    def info(self):
        print("this is a example of maltiple inharitance")
m=vahicle()
m.from_bike()
m.from_bycicle()
m.from_motorcycle()
m.info()'''
class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")
class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The dance is {self.dance}")
class employeedancer(employee,dancer):
   def __init__(self,name,dance):
        # self.name=name                   
        # self.dance=dance  
        super().__init__(name)# Call the employee's __init__ method
        dancer.__init__(self,dance)# Call the dancer's __init__ method
              
o=employeedancer('ajay','garba')
print(o.name)
print(o.dance)
o.show()

#mro()
print(employeedancer.mro())
'''[<class '__main__.employeedancer'>, <class '__main__.employee'>, <class '__main__.dancer'>, <class 'object'>]
 this is out put of the mro()  any method which way find out'''