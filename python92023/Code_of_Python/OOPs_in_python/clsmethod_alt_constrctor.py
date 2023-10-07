class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def printdetails(self):
        print(f"the name of the employee {self.name} and salary is {self.salary}")
    @classmethod
    def fromstringdesh(cls,dash):
        # return cls(dash.split("_")[0],int(dash.split("_")[1])) #this is another way to retern data in spliting
        name,salary=dash.split("_"and "," and " ")
        return cls(name,int(salary))
    @classmethod
    def fromstringinput(cls,data):
         return cls(data.split("-")[0],int(data.split("-")[1]))
    
data=input("Enter the employee name and salary in formate like 'employee-salary in number' ")
e1=employee("ajay",15000)
e1.printdetails()
print("-------------------")
e2=employee.fromstringinput(data)
e2.printdetails()

dash="meena 46000"
e3=employee.fromstringdesh(dash)
e3.printdetails()



