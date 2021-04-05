import shutil
import os

# Set where the source of the files that the user should check daily for new content
source = '/Users/mitchell_estes/Desktop/The Tech Academy/sourceFolder/'

# Set the destination path to destinationFolder where copied files are stored
destination = '/Users/mitchell_estes/Desktop/The Tech Academy/destinationFolder/'

# Defines files that the user will have to check on a daily occurance
files = os.listdir(source)

# Function called by the user that moves files in the source folder to destination
def File_Check():
	# Loops through all the daily files that need to be moved to destination
	for i in files:
		shutil.move(source+i, destination)

# Calling the class
File_Check()
