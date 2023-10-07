# this is example of the operator overloading
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k "
    def __add__(self,x):
        return vector(self.i + x.i,self.j+ x.j,self.k+ x.k)
    # def __add__(self,x):   #__add__ operator overload to '+'
    #     return f" this is magic method  to use on {x}"
v1=vector(7,8,9)
print(v1)
v2=vector(8,4,2)
print(v2)
print(v1+v2)


# this  is operator overriding  or  overloading
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # Define how the '+' operator should work for ComplexNumber objects
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Create two ComplexNumber objects
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 7)

# Use the '+' operator to add them
result = num1 + num2

# Print the result
print(result)  # Output: 3 + 10i





#  note that   this is  example of the method overloading 
'''class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return self._add_two(args[0], args[1])
        elif len(args) == 3:
            return self._add_three(args[0], args[1], args[2])
        else:
            raise ValueError("Invalid number of arguments")

    def _add_two(self, a, b):
        return a + b

    def _add_three(self, a, b, c):
        return a + b + c

calc = Calculator()
result1 = calc.add(1, 2)          # This will call _add_two
result2 = calc.add(1, 2, 3)       # This will call _add_three
'''

