import tkinter as tk

# Creates popup window that allows user to enter text
window = tk.Tk()
# Defines elements that will be on the pop-up window 
label = tk.Label(text="Input Webpage's Text:")
entry = tk.Entry()
button = tk.Button(text="Submit")

# Adds the elements to the pop-up window 
label.pack()
entry.pack()
button.pack()
# Runs the window on a lasting loop (NEED TO FIX)
window.mainloop()
	# Loop until the user enters text on entry and hits submit button
	
	# Sets the string value that will make up the webpage's content
	pageContent = "Change this value to the the text entered into 'entry' when submit button clicked"

# Creates a new HTML file
f = open('newWebpage.html','w')

# The HTML content that will be written to new file
message = "<html><body><h1>" + pageContent + "</h1></body></html>"

# Writes the message to the file and then closes it
f.write(message)
f.close()