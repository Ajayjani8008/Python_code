#read mode
f=open("myfile.txt","r")
data=f.read()
print(data)
f.close()
#write mode
f=open("my_working_file1.txt","w")
f.write("hyyy i'm a python !!!")
f.close()
#append mode
f=open("my_working_file2.txt","a")
f.write("  jay swaminarayan\n")
f.close()

#the another way 
with open("with_as_f.txt","a") as f:
    f.write(" hyyy  i am ajay\n")
