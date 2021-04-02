# Creates parent class called Vehicle 
class Vehicle:
	def __init__(self, vehicleType, electricFuel, numWheels):
		self.vehicleType = vehicleType
		self.electricFuel = electricFuel
		self.numWheels = numWheels
		self.secretMessage = "Let's Go!"

	# Defines a move_vehicle function that prints secretMessage 
	def move_vehicle(self):
		print(self.secretMessage)

	# Defines a function that changes the vehichles secretMessage
	def change_message(self, private):
		self.secretMessage = private

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

# Creates an instance of the class and calls the functions
testVehicle = Vehicle("Vehicle", False, 4)
testVehicle.move_vehicle()
testVehicle.change_message("Secret Message Changed!")
testVehicle.move_vehicle()