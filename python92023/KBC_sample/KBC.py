
Quetions = [["which language use more and more today ? :",
             "python", "java", "cpp", "mojo", 4],
            ["which language use too webdevlopment also ? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language  ? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language use as multiple field ? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language use too less? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language  is new in market ? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language use for AI? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language is morthen faster of python? :",
                "python", "java", "cpp", "mojo", 4],
            ["which language is same as python ? :",
                "python", "java", "cpp", "mojo", 4]]
print("Jay Swaminarayan")
levels = [5000, 10000, 50000, 100000, 500000,
          1000000, 5000000, 10000000, 50000000]
money = 0
for i in range(0, len(Quetions)):
    Quetion = Quetions[i]
    print(f"\nQuestion for Rs.{levels[i]} is :\n{Quetion[0]} ")
    print(f"(a) {Quetion[1]}    (b) {Quetion[2]}    (c) {Quetion[3]}    (d) {Quetion[4]}")
    reply = input("Enter your answer from a-d:")
    if reply == 'a':
        reply = 1
    elif reply == 'b':
        reply = 2
    elif reply == 'c':
        reply = 3
    elif reply == 'd':
        reply = 4
    else:
        print("Enter the option in a,b,c or d...")
    if (reply == Quetion[-1]):
        print(f"you won  Rs. {levels[i]}")
        if (i == 3):
            money = 100000
        elif (i == 6):
            money = 5000000
        elif (i == 8):
            money = 50000000
            print(" Congratulation !!! you are KBC King ...")
    else:
        print("wrong answer.....")
        break
print(f"Your Take home money Rs. {money}  ")
