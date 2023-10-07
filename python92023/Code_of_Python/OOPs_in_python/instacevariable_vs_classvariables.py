class Employee:
    company_name="apple"
    NO_of_employee=0
    def __init__(self,name):
        self.name=name
        self.raise_amont=0.50
        Employee.NO_of_employee+=1
    def show_details(self):
        print(f" the  name of the employee {self.name} and raise of the amount {self.raise_amont} and company name {self.company_name} and in the company have now {self.NO_of_employee} empolyee")

ajay=Employee("ajay")
ajay.company_name="microsoft"
ajay.show_details()

meena=Employee("meena")
meena.raise_amont=0.90
meena.show_details()

