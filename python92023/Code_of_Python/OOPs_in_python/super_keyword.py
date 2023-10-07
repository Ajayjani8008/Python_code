class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def prarent_method(self):
        print(" i am form parent class")
class programmer(employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)# perent class constractor by super key word
        self.lang=lang
    def child_method(self):
        print(" i am form child class")
        super().prarent_method()
        #we can use super keyword to call parent class attributes and method
ajay=programmer("ajay",102,"pthon")
ajay.child_method()
print("------------")
ajay.prarent_method()
print("------------")

print(ajay.name)
print(ajay.id)
print(ajay.lang)
