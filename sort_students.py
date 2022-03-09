import mysql.connector

db_name = "anathaDb"

def sort():
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()

		mycursor.execute("SELECT * FROM student ORDER BY name")
		result = mycursor.fetchall()

		print("\n  student sorted by name in ascending order")
		for i in result:
			print(f"\t{i}")

	except :
		pass

sort()
