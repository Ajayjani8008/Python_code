
Fileptr = open("file1.txt", "w")
Fileptr.write("""ajay is good boy and 
he  learn python""")
Fileptr.close()




fileptr = open("file1.txt", "r")
if fileptr:
    print("file is open succesfully")
fileptr.close()





fileptr=open("file1.txt","a")
fileptr.write("""    \nif you are a coder
then python help you make future easy""")
fileptr.close()

fileptr=open("file1.txt","r")
contant=fileptr.read(100)
print(contant)
fileptr.close()

