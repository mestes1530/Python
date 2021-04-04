import shutil
import os

# Set where the source of the files are
source = 'https://github.com/mestes1530/Python/tree/main/The%20Tech%20Academy/sourceFolder'

# Set the destination path to destinationFolder
destination = 'https://github.com/mestes1530/Python/tree/main/The%20Tech%20Academy/destinationFolder'
files = os.listdir(source)

for i in files:
	# Move the files represented by i to the destination file
	shutil.move(source+i, destination)

