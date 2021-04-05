import shutil
import os

# Set where the source of the files are
source = '/Users/mitchell_estes/Desktop/The Tech Academy/sourceFolder'

# Set the destination path to destinationFolder
destination = '/Users/mitchell_estes/Desktop/The Tech Academy/destinationFolder'
files = os.listdir(source)

for i in files:
	# Move the files represented by i to the destination file
	shutil.move(source+i, destination)
