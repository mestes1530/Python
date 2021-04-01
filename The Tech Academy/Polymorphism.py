# Creates parent class called Vehicle 
class Vehicle:
	def __init__(self, vehicleType, electricFuel, numWheels):
		self.vehicleType = vehicleType
		self.electricFuel = electricFuel
		self.numWheels = numWheels
	# Defines a move_vehicle function for the Vehile 
	def move_vehicle(self):
		print("Let's Go!")


# Creates a child class called Car from parent Vehicle class
class Car(Vehicle):
	def __init__(self, vehicleType, electricFuel, numWheels, carMaker, carModel):
		super().__init__(self, vehicleType, electricFuel, numWheels)
		self.carMaker = carMaker
		self.carModel = carModel

# Creates a child class called Bike from parent Vehicle class
class Bike(Vehicle):
	def __init__(self, vehicleType, electricFuel, numWheels, fixedGear, mountainBike):
		super().__init__(self, vehicleType, electricFuel, numWheels)
		self.fixedGear = fixedGear
		self.mountainBike = mountainBike

# Creates an instance of the class and calls the function
testVehicle = Vehicle("Vehicle", False, 4)
testVehicle.move_vehicle()
