import mysql.connector

status = False

def filter():
	global status
	try:
		db_name = "anathaDb"

		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()
		mycursor.execute("SELECT district FROM student")

		result = mycursor.fetchall()

		# result originaly comming as list of tuple and we need to convert it into list of string on that way its easy to use
		i = 0
		for x in result:
			result[i] = x[0]
			i += 1

		# and now we need to remove duplicates othervise it will show same result mulitiple times
		result = list(dict.fromkeys(result))

		print("\n  Students with same location")
		for x in result:
			mycursor.execute(f"SELECT * FROM student WHERE district = '{x}'")
			data = mycursor.fetchall()
			print(f"\tdistrict: {x}")
			for y in data:
				print(f"\t\t{y}")

		status = True

	except:
		print("An error occured [-]")