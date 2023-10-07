'''class employee:
    name="ajay"
    i=0
    def __len__(self):
        for c in self.name:
            i=i+1
        return i
e=employee()
print(e.name)
print(len(e)) '''  # how  to __len__()  method  define 

''' for  run this file  emp.py must have'''
from emp import employee
e=employee("ajay")
print(e)

print(str(e))# by strs
print(repr(e))  # by repr
print(e())

