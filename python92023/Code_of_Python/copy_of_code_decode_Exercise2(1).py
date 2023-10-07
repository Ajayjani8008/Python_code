

usercode = input("Enter the messeage for convert in to codewrod lenguage.. ")
codes = usercode.split(" ")
command = False
if (command):
    newcode = []
    for code in codes:
        if (len(code) >= 3):
            r1="dff"
            r2="trt"
            neword = r1+code[1:]+code[0]+r2
            newcode.append(neword)
        else:
            newcode.append(code[::-1])
    print(" ".join(newcode))
    
else:
    newcode=[]
    for code in codes:
        if (len(code)>=3):
            newword=code[3:-3]
            newword=newword[-1]+newword[:-1]
            newcode.append(newword)
        else:
            newword=code[::-1]
            newcode.append(newword)
    print(" ".join(newcode))
