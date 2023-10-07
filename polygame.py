class GAME:
    def get_point(self):
        pass

    def dis_point(self):
        pass


class badmintan(GAME):
    def get_point(self):
        badmintan.p1 = int(input("Enter points of badmintan.."))

    def dis_point(self):
        print("total points  of badmintan...", badmintan.p1)


class woliball(GAME):
    def get_point(self):
        woliball.p1 = int(input("Enter points of woliball..."))

    def dis_point(self):
        print("total points  of woliball...", woliball.p1)


class crikat(GAME):
    def get_point(self):
        crikat.p1 = int(input("Enter points of cricket..."))

    def dis_point(self):
        print("total points  of cricket...", crikat.p1 )


bad = badmintan()
bad.get_point()
bad.dis_point()
cri = crikat()
cri.get_point()
cri.dis_point()
woli = woliball()
woli.get_point()
woli.dis_point()
