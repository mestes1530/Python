import shutil
import os
import tkinter as tk

# Function conducts the file transfer process when file paths are entered and button clicked
def Submit():
	# Defines file locations and their contents
	source = sourceEntry.get()
	destination = destinationEntry.get()
	files = os.listdir(source)
	archives = os.listdir(destination)
	# Loops through the files in source folder and moves them
	for i in files:
		shutil.move(source+i, destination)

# Creates popup window that allows user to enter file paths and run file transfer
window = tk.Tk()

# Defines elements that will be on the pop-up window 
sourceLabel = tk.Label(text="Enter path to sourceFolder: ")
sourceEntry = tk.Entry()
destinationLabel = tk.Label(text="Enter path to destinationFolder: ")
destinationEntry = tk.Entry()
button = tk.Button(text="Run File Transfer", command=lambda:Submit())

# Adds the elements to the pop-up window 
sourceLabel.pack()
sourceEntry.pack()
destinationLabel.pack()
destinationEntry.pack()
button.pack()

# Runs the window on a lasting loop
window.mainloop()

