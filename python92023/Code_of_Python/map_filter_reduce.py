def quards(x):
    return x*x*x*x

l=[5,5,6,37,48,8,59,0,56]
newl=[]
for i in l:
    newl.append(quards(i))
    
print(newl)
#by using map method  we can do this

newl2=list(map(quards,l))
print(newl2)

# FILTER
filtered_list=list(filter(lambda x:x>10,l))
print(filtered_list)
# if any function take another function as argument then it's fonction call higher order funcion

# now we familier to reduce function
from functools import reduce
number=[1,2,3,4,5,6,7,8,9,10]
def my_opration(a,b):
    return a+b
    

reduced_results=reduce(my_opration,number)
print(reduced_results)
