class Employee:
    def __init__(self, emp_no, emp_name, dept_name, salary, TA, DA, PF, net_salary):
        Employee.emp_no = emp_no
        Employee.emp_name = emp_name
        Employee.dept_name = dept_name
        Employee.salary = salary
        Employee.TA = TA
        Employee.DA = DA
        Employee.PF = PF
        Employee.net_salary = net_salary

        Employee.TA = Employee.salary*0.1
        Employee.DA = Employee.salary*0.08
        Employee.PF = Employee.salary*0.05
        Employee.net_salary = (Employee.TA+Employee.DA +
                               Employee.salary)-Employee.PF

    def disply(self):
        print("employee number is :", Employee.emp_no)
        print("employee name is :", Employee.emp_name)
        print("employee department name is :", Employee.dept_name)
        print("employee salary is :", Employee.salary)
        print("employee TD is :", Employee.TA)
        print("employee DA is :", Employee.DA)
        print("employee PF is :", Employee.PF)
        print("employee net salary is :", Employee.net_salary)
s1=Employee(10,"ajay","math",10000,1,1,1,1)
s1.disply()
