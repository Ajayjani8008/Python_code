# ____________________this is seek and tell method___________________________
with open("ajay.txt","r") as f:
    print(type(f))
    f.seek(10)
    #go to  on 10th byte's charchter  in the file
    # for read the next 5 bytes 
    print(f.tell())
    
    data=f.read(5)
    print(data)
    
    
    # seek method : go to nth bytes position
    # tell methof : give curser position 
    #                 tell that which position seek now 
# _________________________truncated method________________________________

with open("truncated.txt","w") as ajay:
    ajay.write("hii ajay this  is a file which you truncated")
    ajay.truncate(10)
    # apply limit  after nth character we can not add more 
    # also make file size as we choose and we maintain our file size 
with open("truncated.txt","r") as ajay:
    
    ajay2=ajay.read()
    print(ajay2)