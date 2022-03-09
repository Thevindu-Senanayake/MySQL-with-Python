import mysql.connector

status = False

def update_records():
	global status
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database="anathaDb"
		)

		mycursor = db.cursor()

		# names
		name_cmd = f"UPDATE student SET name = %s WHERE name = %s"
		name_data = [
			("sarah", "angammana sumana"),
			("jhon", "samantha"),
			("jack", "buruwa"),
			("lily", "sara"),
			("maya", "winkale")
		]

		# email
		email_cmd = f"UPDATE student SET email = %s WHERE email = %s"
		email_data = [
			("sarah@anatha.com", "angammana_sumana@anatha.com"),
			("jhon@modaya.lk", "samantha@modaya.lk"),
			("jack@burupetiya.org", "buruwa@burupetiya.org"),
			("lily@polleli.org", "sara@polleli.org"),
			("maya@uncle.org", "winkale@uncle.org")
		]

		mycursor.executemany(name_cmd, name_data)
		mycursor.executemany(email_cmd, email_data)

		print(f"\nRecords updated successfully [+]")
		db.commit()
		status = True
	except:
		print("unable to update records [-]")
