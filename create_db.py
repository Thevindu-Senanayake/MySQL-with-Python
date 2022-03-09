import mysql.connector

status = False

# Create database if not exists
def createDb():
	global status
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd=""
		)

		mycursor = db.cursor()

		mycursor.execute('create database if not exists anathaDb')
		print("Database created [+]")
		status = True
	except:
		print("unable to create database [-]")
