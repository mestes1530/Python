# Creates parent class called Vehicle 
class Vehicle:
	def __init__(self, vehicleType, electricFuel, numWheels):
		self.vehicleType = vehicleType # Public Attribute
		self.electricFuel = electricFuel # Public Attribute
		self.numWheels = numWheels # Public Attribute
		self._secretMessage = "Let's Go!" # Private Attribute

	# Defines a move_vehicle function that prints secretMessage 
	def move_vehicle(self):
		print(self._secretMessage)

	# Defines a function that changes the vehichles secretMessage
	def change_message(self, private):
		self._secretMessage = private

# Creates a child class called Car from parent Vehicle class
class Car(Vehicle):
	def __init__(self, vehicleType, electricFuel, numWheels, carMaker, carModel):
		super().__init__(self, vehicleType, electricFuel, numWheels)
		self._carMaker = carMaker # Private Attribute
		self._carModel = carModel # Private Attribute

# Creates a child class called Bike from parent Vehicle class
class Bike(Vehicle):
	def __init__(self, vehicleType, electricFuel, numWheels, fixedGear, mountainBike):
		super().__init__(self, vehicleType, electricFuel, numWheels)
		self.fixedGear = fixedGear # Public Attribute
		self.mountainBike = mountainBike # Public Attribute

# Creates an instance of the class and calls the functions (should be replaced w/ below for assignment)
testVehicle = Vehicle("Vehicle", False, 4)
testVehicle.move_vehicle()
testVehicle.change_message("Secret Message Changed!")
testVehicle.move_vehicle()

# BOTH STATEMENTS BELOW BREAK IT FOR SOME REASOM?
#testCar = Car("Car", False, 4, "Ford", "Ranger")
#testBike = Bike("Bike", False, 2, True, False)

# WOULD USE CODE BELOW (INSTEAD) IF ABOVE STATEMENTS WORKED 
#testCar.move_vehicle()
#testCar.change_message("Message Changed To Car!")
#testCar.move_vehicle()
