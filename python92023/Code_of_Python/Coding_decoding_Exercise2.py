st = input("Enter message... ")
words = st.split(" ")
coding = False
# coding= True
if (coding):
    nword = []
    for word in words:
        if (len(word) >= 3):
            r1 = "mmm"
            r2 = "nnn"
            stnew = r1+word[1:]+word[0]+r2
            nword.append(stnew)
        else:
            nword.append(word[::-1])
    print(" ".join(nword))
else:
        nword = []
        for word in words:
            if (len(word) >= 3):
                stnew = word[3:-3]
                stnew=stnew[-1]+stnew[:-1]
                nword.append(stnew)
            else:   
                nword.append(word[::-1])
        print(" ".join(nword))
