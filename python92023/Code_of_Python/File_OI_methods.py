# _______________________readlines_______________________
# f=open("my_working_file2.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
# f.close()
    
# f=open("my_working_file1.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
# f.close()


# f=open("ajay.txt","r")
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)
# ---------------------------formation marks with by readlines---------------------------
# f=open("Marks_student.txt","r")

# while True:
#     line=f.readline()
#     if not line:
#         break
#     name=line.split(",")[0]
#     m1=int(line.split(",")[1])
#     m2=int(line.split(",")[2])
#     m3=int(line.split(",")[3])
#     m4=int(line.split(",")[4])
#     m5=int(line.split(",")[5])
#     m6=int(line.split(",")[6])
#     m7=int(line.split(",")[7])
#     m8=int(line.split(",")[8])
#     m9=int(line.split(",")[9])
#     m10=int(line.split(",")[10])

#     print(f"marks of the student {name} in maths is : {m1}")
#     print(f"marks of the student {name} in scince is : {m2}")
#     print(f"marks of the student {name} in chemistry is : {m3}")
#     print(f"marks of the student {name} in fgdfg is : {m4}")
#     print(f"marks of the student {name} in chemifgdstry is : {m5}")
#     print(f"marks of the student {name} in chemistdgdry is : {m6}")
#     print(f"marks of the student {name} in chemistrygdg is : {m7}")
#     print(f"marks of the student {name} in chemistrygdg is : {m8}")
#     print(f"marks of the student {name} in chemistrygdg is : {m9}")
#     print(f"marks of the student {name} in chemistrygdg is : {m10}")
f=open("my_working_file1.txt","w")
line=["ajay\n","jani\n"]
f.writelines(line)
f.close() 

    