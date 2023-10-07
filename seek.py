fileptr=open("file2.txt","r")
print("the pointer is at byte:",fileptr.tell())
content=fileptr.read()
print("after reading ,the file pointer ia at:",fileptr.tell())
fileptr.seek(200)
print("""after the seek funtion use
 our pointer  is seek at :""",fileptr.tell())
contant=fileptr.read(200)
print(contant)
