import shutil
import os

# Set where the source of the files that the user should check daily for new content
source = '/Users/mitchell_estes/Desktop/The Tech Academy/sourceFolder/'

# Set the destination path to destinationFolder where copied files are stored
destination = '/Users/mitchell_estes/Desktop/The Tech Academy/destinationFolder/'

# Defines files that the user will have to check on a daily occurance
files = os.listdir(source)

archives = os.listdir(destination)

# Function called by the user that moves files in the source folder to destination
def File_Check():
	# Loops through all the daily files that need to be moved to destination
	for i in files:
		shutil.move(source+i, destination)

# User prompts detailing the file transfer in text
print("Files in sourceFolder: { " + files[0] + ", " + files[1] + ", " + files[2] + " }\n")
print("Files in destinationFolder: { }\n")
print("Press 'Enter' to run the daily file transfer:\n")
x = input() # Breaks here, tried a variation of input statements
print("Input was successfully entered")


# Calling the function
File_Check()
