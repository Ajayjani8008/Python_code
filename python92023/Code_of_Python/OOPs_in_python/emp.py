class employee:
    '''this class join to "dander_magic_method.py"'''
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"the name of employee {self.name} by __str__"
    def __repr__(self):
        return f"the name of the employee {self.name} by __repr_"
    def __call__(self):
        return f"hyy i am man"
    