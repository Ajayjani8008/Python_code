class cricketer:
    def datainput(self):
        cricketer.Name = input("Enter name of the crickter:")
        cricketer.Age = int(input("Enter Age of the crickter:"))
        cricketer.total_score = int(
            input("Enter toatal scrore of the crickter:"))
        cricketer.total_match_played = int(
            input("Enter total match played  crickter:"))
        cricketer.Centuries = int(input("Enter Centuries of the crickter:"))
        cricketer.Fifties = int(input("Enter Fifties of the crickter:"))
        cricketer.Avg = ((cricketer.total_score) /
                         (cricketer.total_match_played))

    def display_data(self):
        print("Name of the crickter.... ", cricketer.Name)
        print(cricketer.Name, "'s  Age is...", cricketer.Age)
        print(cricketer.Name, "'s toatal scrore :", cricketer.total_score)
        print(cricketer.Name, " total",
              cricketer.total_match_played, " match played")
        print("total", cricketer.Centuries, " Centuries  by  ", cricketer.Name)
        print("total", cricketer.Fifties, " Fifties by  ", cricketer.Name)
        print("  average  of ", cricketer.Name,
              "'s all match is..", cricketer.Avg)


P1 = cricketer()
P1.datainput()
P1.display_data()
P2 = cricketer()
P2.datainput()
P2.display_data()
P3 = cricketer()
P3.datainput()
P3.display_data()

P4 = cricketer()
P4.datainput()
P4.display_data()
P5 = cricketer()
P5.datainput()
P5.display_data()
