# # jay swaminarayan

# # the example of  getter and setter by useing @property
# class Employee():
#     def __init__(self, value, name):
#         self._value = value
#         self._name = name

#     def show_details(self):
#         print("------------------------")
#         print(f"the value is {self._value}")
#         print(f"the value is {self._name}")

#     @property
#     def _getter_(self):
#         return self._value, self._name

#     @_getter_.setter
#     def _getter_(self, values):
#         self._value, self._name = values


# a = Employee(10000, "jay swaminarayan")
# a.show_details()
# print(a._value)  # normaly acess value
# print(a._getter_)  # by use of @property and getter method

# a._getter_ = (454, "ajay")
# print(a._getter_)
# a.show_details()

# jay swaminarayan
class student():
    def __init__(self,name,standard,result):
        self.name=name
        self.standard=standard
        self.result=result
    def print_student_details(self):
        print("____________")
        print(f"name of the student is {self.name},standard of the student is {self.standard} and the final result of the student is {self.result}")
    @property
    def student_details(self):
        return self.name,self.standard,self.result
    @student_details.setter
    def student_details(self,values):
        self.name,self.standard,self.result=values
        
        
student1=student("Ajay","12th",97.45)
student1.print_student_details()# print the values by print_student_details  method
print(f"----{student1.name}---{student1.standard}---{student1.result}----")#Normally get the values
print(student1.student_details)# print and get values by getter
student1.student_details=("mahesh","11th",99.90)# set the all student details by setter property
student1.print_student_details()#print the all student details useing class's method

