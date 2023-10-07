#the basic example od the lambda function

# def ajay(x):
# #     return x*2
# ajay=lambda x:x*2
# print(ajay(100))

# def machine(fx,value):
#     return 6+fx(value)

# print(machine(ajay,10))



# in the other word 
# # we can also that 

# def my_self(fx,values):
#     return fx(values)+values

# print(my_self(lambda x:x*100,88))


def fun_as_arg(fx,price):
    new_price=price+price*(0.40) 
    return new_price-fx(new_price)
price=int(input("Enter your price original : "))   
print(fun_as_arg(lambda x:x*(0.40),price))
    