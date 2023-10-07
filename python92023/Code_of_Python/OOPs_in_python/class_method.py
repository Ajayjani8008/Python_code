class employee:
    companyname="apple"
    def __init__(self,name):
        self.name=name
    def showdetails(self):
        print(f"the name of employee is {self.name} and his company is {self.companyname}")
    @classmethod #refrace  to class  not instance
    def changecompany(cls,newcompany): # we can use any word replce of self ,python accept it as self.cls-->self by example
        cls.companyname=newcompany

        


    
a1=employee("ajay")
a1.showdetails()
a1.changecompany("tesla")
a1.showdetails()
print(employee.companyname)
