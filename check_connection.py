import mysql.connector

status = False

def check_connection():
	global status
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd=""
		)

		if db.is_connected():
			print("Connected to MySQL database [+]")
			status = True
	except:
		print("Unable to connect to MySQL database check if mysql server is running on defaul port which is 3306 [-]")
