
class polygon():
    #abtract method
    def sides(self):
        pass
class triagle(polygon):
    def sides(self):
        print('triangle has 3 sides...')
class ractangle(polygon):
    def sides(self):
        print("rectagle has 4 sides...")
class sqare(polygon):
    def sides(self):
        print("sqare has 4 sides all are same....")
class pentagon(polygon):
    def sides(self):
        print("pentagon has 5 sides ....")

#driver code
t=triagle()
s=sqare()
r=ractangle()
p=pentagon()
t.sides()
s.sides()
p.sides()
r.sides()


