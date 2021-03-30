# Creates a test databse, fills it with the text from .txt files and then prints the contents

# Imports SQLlite
import sqlite3

# Creates a Dtatabase called test.db
conn = sqlite3.connect('test.db')

# Creates a table w/ a primary integer field and a text field that holds the contentas of .txt files 
with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS tb1_texts( \
		ID INTEGER PRIMARY KEY AUTOINCREMENT, \
		col_text TEXT \
		)")
	conn.commit()
conn.close()

# Confirms using the correct database
conn = sqlite3.connect('test.db')

# Variable containing file names that need to be considered
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
	'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Loop through files and only add the files ending in .txt
for x in range(len(fileList)):
	if fileList[x].endswith('.txt'):
		# Opens the .txt file
		file = open(fileList[x])
		# Puts all text on one line and closes the file
		line = file.read().replace("\n", " ")
		file.close()
		# Gets the cursor ready to add to the database
		cur = con.cursor()
		# Adds the text content to the databse
		cur.execute("INSERT INTO tb1_texts(col_text) VALUES (?)", \
			(line))
		conn.commit()

# Confirms using the correct database
conn = sqlite3.connect('test.db')

# Prints the text content from the database
with conn:
	cur = conn.cursor()
	# Selects the relevent columns from the table
	cur.execute("SELECT col_text FROM tb1_texts")
	varText = our.fetchall()
	for item in varText:
		msg = "File Text: ()".format(item[0])
	# Prints the text contents
	print(msg)




