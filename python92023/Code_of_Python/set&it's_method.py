# ajay=set() # this is a empty set 
# print(type(ajay))
# ajay={}  # this is dictonary

# ghanshyam={"jay swaminarayan ",12,2,3,4,5}
# for value in ghanshyam:
#     print(value)
    
# print(ghanshyam)

# s1={1,3}
# s2={1,4,57,8,3,578,26,67}
# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.update(s2)
# print(s1,s2)

# ajay=s1.intersection(s2)

city1={"dihor","talaja","bhavnagar","timana","royal"}
city2={"palitana","mahuva","bhavnagar","dihor"}
# city3=city1.intersection(city2)
# print(city3)

# print(city1)
# city1.intersection_update(city2)
# print(city1)

# result=city1.symmetric_difference(city2)
# print(result)
# city1.symmetric_difference_update(city2)
# print(city1)

# city1.difference(city2)
# print(city1)

print(city1.isdisjoint(city2))
city3={"this ","ajay","jani","ajay"}
city4={"ajay","jani"}
print(city3.issuperset(city4))
print(city4.issubset(city3))

city1.add("my name is ajay")
print(city1)
city1.remove("timana")
print(city1)
city1.discard("adfksdfkj")
print(city1)
del city1 # delete  hall set


if "bhavnagar" in city2:
    print(" bhavnagar  is  in there  ")
else: 
    print("bhavnager is not in set ")