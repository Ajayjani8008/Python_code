
N=int(input("enter the number:"))
for i in range(1,N+1):
     if i % 2 == 0:
        evenfile=open("even_file.txt","a")
        evenfile.write(str(i))
        evenfile.close()
     else:
        oddfile=open("odd_file.txt","a")
        oddfile.write(str(i))
        oddfile.close()



       


