import random
Computer_score=0
Player_score=0
def check(Player1,Player2):
        if (Player1 == Player2):
            return 0
        elif (Player1 == "S" and Player2 =="W" ) or (Player1 == "W" and Player2 == "G") or(Player1 == "G" and Player2 == "S"):
            return -1
        else:
            return 1
for _ in range(7):
    Computer = random.choice(["S","W","G"])
    
    while True:
        Player = input(
            "--------------------------------\n Choose your choice  in follow :\n S for snak \n W for water\n G for gun \n")
        Player=Player.upper()
        if Player in ["S","W","G"]:
            break
        else:
            print("Invalid Input! Please enter S, W, or G.")
    print("Computer choice :", Computer)  
    print("Your choice :", Player)  
    score = check(Computer, Player)
    if score==0:
        print("It's a Tie!")
    elif score==-1:
        print("Computer wins!")
        Computer_score += 1
    elif score==1:
        print("You wins!")
        Player_score += 1
print("__________________________________","\n")   
print("Computer  Score :",Computer_score)
print("Player  Score",Player_score,"\n")  
print("**********************************")
if (Player_score > Computer_score):
    print("Congratulations!you are winner")
elif (Player_score == Computer_score):
    print("It's a tie overall.")
elif (Player_score < Computer_score):
    print("Sorry, you lost the game.")