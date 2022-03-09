import mysql.connector

db_name = "anathaDb"
status = False

def delete():
	global status
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()

		# maths
		mycursor.execute("SELECT * FROM marks")
		result = mycursor.fetchall()

		for row in result:
			if row[2] < 40:
				cmd = f"DELETE FROM marks WHERE maths = {row[2]}"
				mycursor.execute(cmd)

		# science
		for row in result:
			if row[3] < 40:
				cmd = f"DELETE FROM marks WHERE science = {row[3]}"
				mycursor.execute(cmd)

		# ict
		for row in result:
			if row[4] < 40:
				cmd = f"DELETE FROM marks WHERE ict = {row[4]}"
				mycursor.execute(cmd)

		# english
		for row in result:
			if row[5] < 40:
				cmd = f"DELETE FROM marks WHERE english = {row[5]}"
				mycursor.execute(cmd)

		print("\nAll Students with marks less than 40 have been deleted in marks table [+]")
		db.commit()
		status = True

	except:
		print("An error occured [-]")
