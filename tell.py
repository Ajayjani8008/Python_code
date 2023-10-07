fileptr=open("file2.txt","r")
print("the pointer is at byte:",fileptr.tell())
content=fileptr.read()
print("after reading ,the file pointer ia at:",fileptr.tell())
