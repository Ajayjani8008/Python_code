
# the use of the enumerate funcion to get  value with   index  
# and update and enumerate index automatically
marks = [134, 346, 554, 534, 232, 322, 323, 233, 326, 323, 236]
index = 0
for mark in marks:
    print(mark)
    if (index == 4):
        print("jay swaminarayan")
    index += 1 # with out use  the enumerate function
    
    #  for the another way ... we use anumerate function
    
for index,mark in enumerate(marks, start=1):#first for indexing and other one for value
    print(mark)
    if index==4:
        print("jay harikrushn maharaj") 
        
        
        


