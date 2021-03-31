# Creates parent class called Vehicle 
class Vehicle:
	def __init__(self, vehicleType, electricFuel, numWheels):
		self.vehicleType = vehicleType
		self.electricFuel = electricFuel
		self.numWheels = numWheels

# Creates a child class called Car from Vehicle class
class Car(Vehicle):
	def __init__(self, vehicleType, electricFuel, numWheels, carMaker, carModel):
		super().__init__(self, vehicleType, electricFuel, numWheels)
		self.carMaker = carMaker
		self.carModel = carModel



	