# x=[1,2,34,4,5]
# print(dir(x))
# print(x.__add__)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
# 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 
# 'sort'] # this are method on list  
# for tuple
# y=(1,2,3,4,5,6,7,6)
# print(dir(y))
# print(y.__add__) 
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index'] # this method for tuple
# <method-wrapper '__add__' of tuple object at 0x00000240A300CD60>


# __dict__ method  

class person :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        self.version=1
    def info_person(self):
        print(" jay swaminarayan")
bramin=person("Ajay",25)
print(bramin.__dict__)


#help method  

print(help(person))
print(help(str)) # gives all info releted  string 

