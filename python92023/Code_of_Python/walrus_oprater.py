'''a=True
print(a=False) #this get an error

print(a:=False) # this is walrus operter example 


# Without the walrus operator
n = 10
if n > 5:
    print("The number is greater than 5:", n)

# With the walrus operator
if (n := 10) > 5:
    print("The number is greater than 5:", n)


n = 0

while (n := n + 1) <= 5:
    print("Current value of n:", n)

print("Loop finished. Final value of n:", n)
'''



foods=list()
while (food:=input("give any food name ... "))!="quit":
    foods.append(food)
print(foods)
    