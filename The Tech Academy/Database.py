# Creates a test databse and fills it with user's first, last names and email

import sqlite3

conn = sqlite3.connect('test.db')

with conn:
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS tb1_persons( \
		ID INTEGER PRIMARY KEY AUTOINCREMENT \
		col_fname TEXT, \
		col_lname TEXT, \
		col_email TEXT \
		)")
	conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
	cur = con.cursor()
	cur.execute("INSERT INTO tb1_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
		('Sarah', 'Jones', 'sjones@gmail.com'))
	cur.execute("INSERT INTO tb1_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
		('Sally', 'May', 'sallymay@gmail.com'))
	cur.execute("INSERT INTO tb1_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
		('Kevin', 'Bacon', 'kbacon@rocketmail.com'))
	conn.commit()

	conn = sqlite3.connect('test.db')

	with conn:
		cur = conn.cursor()
		cur.execute("SELECT col_fname,col_lname,col_email FROM tb1_persons WHERE col_fname = 'Sarah'")
		varPerson = our.fetchall()
		for item in varPerson:
			msg = "First Name: ()\nLast Name: ()\nEmail: ()".format(item[0].item[1].item[2])
		print(msg)