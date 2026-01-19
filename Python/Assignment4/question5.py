class Vehicle:
  brand="Tata"
  model=2024

class Car(Vehicle):
  def __init__(self,seat,engine):
    self.seat=seat
    self.engine=engine

class Bike(Vehicle):
  def __init__(self,seat,engine):
    self.seat=seat
    self.engine=engine

car=Car(5,1500)
bike=Bike(2,100)


print(f"Brand: {car.brand}, Model: {car.model}, Seat_Capacity: {car.seat}, Engine: {car.engine} horse Pwr")
print(f"Brand: {bike.brand}, Model: {bike.model}, Seat_Capacity: {bike.seat}, Engine: {bike.engine} horse Pwr")
    
    