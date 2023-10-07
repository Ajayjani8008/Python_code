def factorial(m):
    result = 1
    for i in range(1, m+1):
        result *= i
    return result


a = int(input("Enter the a positive integer number :"))

if a < 0:
    print("Factorial is not for negative number !!!")
else:
    for i in range(1, a+1):
        print(f"the factorial of {i} is {factorial(i)}")



def facto(n):
    factorial_num=1
    for i in range(1,n+1):
        factorial_num*=i
    return factorial_num
    


b=int(input("Enter the number  b :"))
if b<0 :
    print("Enter the positive numbr")
else:
    for i in range(1,b+1):
        print(f"the factorial of {i} is = {facto(i)}")