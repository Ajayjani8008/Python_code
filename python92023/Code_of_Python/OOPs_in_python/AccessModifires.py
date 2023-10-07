#jay swaminarayan
 
#note that in python there is no any thing  that public privet protected 
# all are by default in public 
# if '__' use then it take python as privet and do manging on it atrtibute
#also before attruibute name we join wiht '_' then it's behave as protected attribute but it same as public give as totally out side of the class  
class Employee:
    def Print_my_name(self):
        print("my name is ajay")
        
    def __init__(self):
        self.name='ajay jani'
        self.__password="123456"
        self.__id=101
class programmer(Employee):
    def __init__(self):
        self._field="python developer"
Ajaykumar=Employee()
print(Ajaykumar.name)
# print(Ajaykumar.__password) #can not be access becouse __password in preivet  note that '__'denote that it's privet attribute of the class
# we can access this way....

print(Ajaykumar._Employee__password)#indirectly
print(Ajaykumar._Employee__id)#it's call name mangling in python

print(Ajaykumar.__dir__())
pro1=programmer()
print(pro1._field)
pro1.Print_my_name()
