class person2:
    pass


# class defiantion cannot 
# be empty but some reason you creat it then 
# we punt in the class
# contant by pass  statment
class person:
    def __init__(tont, name, age):
        # replce by self we can replce any word for self
        # but is is \n same for first parameter of the classes
        tont.name = name
        tont.age = age

    def myfun(tont):
        print("hello my name is  ", tont.name, "my age is ", tont.age)


p1 = person("ajay", 45)
p1.myfun()
del p1.age#delete age of the class  by del function
print(p1.age)
