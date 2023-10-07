
# def greet(fx):
#     def mfx():
#         print("good morning jay swaminarayan")
#         fx()
#         print("thank you for useing this function")
#     return mfx
# @greet
# def hello():
#     print("hallo world how are  you !")
# hello()

# def jani(any_fun):
#     def decorated_fun():
#         print("hello how are you \n welcome the new adventure world")
#         any_fun()
#         print("this is your world  enjoy and be happy")
#     return decorated_fun


# @jani
# def ajay():
#     print("my name is ajay")

# ajay()

# # the replacement od the @jani  is follow
# # also we do this
# jani(ajay)()


# if any function have arguments then we must can follow changes
# def decorater(fx):
#     def cdecorater(*args, **kwargs):
#         print(" this is parameterize decorater")
#         fx(*args,**kwargs)
#         print(" thank you for read  this example")
#     return cdecorater
# @decorater
# def addition(a,b,c):
#     print(" The sum of the 3 number is",a+b+c)
# addition(1,3,4)

# we see another example
totle_amount=int(input("Enter the totle amount "))
pf=int(input("Enter the your pf "))
room_amount=int(input("Enter the room_amount "))
Expenditure=int(input("Enter the Expanditure  "))
light_bill=int(input("Enter the light_bill "))

def decorate_saving_fun(function):
    def the_decorate(*args, **kwargs):
        print("your saving money calculateing in  repees...")
        function(*args, **kwargs)
        print("please carefully maneage your Expanditure to save more money \n Thank you!")
    return the_decorate


@decorate_saving_fun
def savings(*args, **kwargs):
    print(totle_amount-pf-room_amount-Expenditure-light_bill)
    
savings(pf,totle_amount, room_amount, Expenditure, light_bill)
