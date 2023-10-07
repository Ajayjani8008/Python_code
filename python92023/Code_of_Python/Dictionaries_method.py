# ajay = {100: "ajay",
#         101: "meena",
#         102: "bhdresh",
#         103: "mehul",
#         104: "bhavesh"}
# print(ajay[101])
# print(ajay)
# print(ajay.get('ajaydf'))
# print(ajay.keys())
# print(ajay.values())

# for key in ajay.keys():
#     print(f"the value corrsponding to {key} is {ajay[key]}")
    
    
    
# print(ajay.items())


# for key ,value in ajay.items():
#     print(f"{key},{value}")



ajay = {100:100101,
        101: 34923,
        102: 2348,
        103: 3498273,
        104: 23497} 
vishal = {1345:106450101,
        1341: 3495423,
        10442: 2364568,
        10344: 459845273,
        1044:423497} 

ajay.update(vishal)
print(ajay) 
 
vishal.clear()  # only clear  dictionary
# del vishal  totally delete
print(vishal)

    
mahamah={}
print(mahamah)

print(ajay.pop(100))
print(ajay)


print(ajay.popitem())
print(ajay)

del ajay[101]
print(ajay)


    
    
          
    

