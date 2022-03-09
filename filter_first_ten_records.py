import mysql.connector

db_name = "anathaDb"

status = False

def filter():
	global status
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()

		mycursor.execute("SELECT total FROM marks")

		result = mycursor.fetchall()

		# this list contain the makrs that fetch from database in intiger form
		marks = []
		for x in result:
			marks.append((x[0]))

		marks_in_descending_order = sorted(marks, reverse=True)
		first_ten_in_marks = marks_in_descending_order[:10]
		duplicate_removed_marks = list(dict.fromkeys(first_ten_in_marks))

		# 1. select the records that marks eqauls to values in first_ten_in_marks and make new list of it
		# 2. i have to remove duplicates in "first_ten_in_marks" because as a example if the first_ten_in_marks is [20, 20, 80, 90, 40, 60, 50] and
		# 	 amara, nayana both got 20 in first iteration both of them are selected and second iteration both of them are selected again
		print("\n  First ten students with highest marks:")
		for x in duplicate_removed_marks:
			mycursor.execute(f"SELECT * FROM marks WHERE total = {x}")
			result = mycursor.fetchall()
			for y in result:
				print(f"\t{y}")

		status = True

	except:
		print("An error occured [-]")
