import tkinter as tk
import webbrowser

# Function that adds text in the entry field to newWebpage.html
def Submit():
	# Gets the inputed text from the entry field and saves it
	pageContent = entry.get()
	# Creates a new HTML file
	f = open('newWebpage.html','w')
	# The HTML content that will be written to new file
	message = "<html><body><h1>" + pageContent + "</h1></body></html>"
	# Writes the message to the file and then closes it
	f.write(message)
	f.close()
	webbrowser.open("newWebpage.html")

# Creates popup window that allows user to enter text
window = tk.Tk()
# Defines elements that will be on the pop-up window 
label = tk.Label(text="Input Webpage's Text:")
entry = tk.Entry()
button = tk.Button(text="Submit", command=lambda:Submit())

# Adds the elements to the pop-up window 
label.pack()
entry.pack()
button.pack()

# Runs the window on a lasting loop
window.mainloop()
