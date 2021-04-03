# Imports Vehicle class from Encapsulation.py file
from Encapsulation import Vehicle

# Defines child class called Car
class Car(Vehicle):
	# Abstract method that changes the change_message function
	#@abstractmethod # (BREAKS CODE FOR SOME REASON?)
	def change_message(self):
		# Sets _secretMessage to a uniique string
		self._secretMessage = "Message Changed Abstractly!"
		print(self._secretMessage)

	# Regular method that gets the number of wheels on the vehicle
	def get_wheel_count(self):
		print(self.numWheels)

# Creates a new object thats an instance of Car class
newCar = Car("Car", False, 4)
# Calls abstract function, change_message
newCar.change_message()
# Calls normal function, get_wheel_count
newCar.get_wheel_count()
