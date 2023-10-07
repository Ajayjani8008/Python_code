class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


w = person("ajay", "jani")
w.printname()


class student(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)


r = student("jani", "ajay",2022)
r.welcome()

