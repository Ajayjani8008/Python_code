#SIMPLE INHERITANCE
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id   
    def shoWdetails(self):
            print(f"The name of the employee is {self.name} and id is {self.id}")  
        
class programmer(Employee):
    def simple_inheritance(self):
        print("This is example of the simple inheritance")
        print(" I am a programmer")
      
e1=Employee("Ajay",101)
e1.shoWdetails()
e2=Employee("vishal",102)
e2.shoWdetails()

p1=programmer("bhavesh",34)
p1.shoWdetails()
p1.simple_inheritance()