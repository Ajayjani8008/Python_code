from functools import reduce


num=["1","2","45",67,78,26,68,"27",366,67,89]
list1=list(map(int,num)) 
num2=[1,2,45,67,78,26,68,27,366,67,89]
print(list1)
list2=reduce(lambda a,b:a+b,num2)
print(list2)


