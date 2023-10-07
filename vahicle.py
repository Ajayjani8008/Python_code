class vehicle:
    def information(self):
        vehicle.color=input("Enter the color of the vahicle:")
        vehicle.vahicle_no=input("Enter the  vahicle number:")
        print("COLOR OF THE VEHICLE IS :",vehicle.color)
        print("NUMBER OF THE  VEHICLE IS :",vehicle.vahicle_no)
class scooter(vehicle):
    def scooterinfo(self):
        scooter.type=input("ENter the type of the scooter bike or moped:")
        scooter.price=int(input("ENter the price of scooter: "))

class Bill:
    def bill(self):

        Bill.disonP=scooter.price*0.07
        Bill.tax=scooter.price*0.04
        print("after main dis. value is",)




class Payment(scooter,Bill):
    def adddis(self):
        if scooter.type=="bike":
            Payment.f_dis=Bill.disonP*(0.03)
            Payment.total_amt=scooter.price-Bill.disonP*(0.03)
        elif scooter.type=="moped":
            Payment.adddis1=scooter.price*(0.02)
            Payment.total_amt2=scooter.price-Payment.adddis1

    def disply(self):
        print("after discou")

     
        

