fifawordcup=open("file2.txt","a")
if fifawordcup:
    print("file is succesfully created")
fifawordcup.write("""messi vs ronaldo the file war
you can not justies ago that 
who are win the wordcup
champian brazil nock out in the wordcup """)
fifawordcup=open("file2.txt","r")

contant=fifawordcup.readlines()
print(contant)
fifawordcup.close()
