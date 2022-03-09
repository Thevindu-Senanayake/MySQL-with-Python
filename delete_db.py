import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="anathaDb"
)

cursor = db.cursor()

cursor.execute("DROP DATABASE anathaDb")