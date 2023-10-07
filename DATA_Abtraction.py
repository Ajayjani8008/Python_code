# abtract base class work



class Car():
    def mileage(self):
        pass#this is type of virtul funtion
    # and it's call data abtracion(hideing)


class maruti_suzuki(Car):
    def mileage(self):
        print("the mileage is 100KMph...")


class BMW(Car):
    def mileage(self):
        print("the mileage is 78KMph...")


class rolsroy(Car):
    def mileage(self):
        print("the mileage is 59KMph...")


class toyta(Car):
    def mileage(self):
        print("the mileage is 90KMph...")


# driver code
M = maruti_suzuki()
M.mileage()

B = BMW()
B.mileage()

R = rolsroy()
R.mileage()

T = toyta()
T.mileage()
