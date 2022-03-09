import mysql.connector

db_name = "anathaDb"
status = False

def seed_data():
	global status
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()

		table_name = "student & marks"

		# :1 name, :2 district, :3 phone, :4 email, :5 age
		student_cammand = "INSERT INTO student (name, district, phone, email, age) VALUES (%s, %s, %s, %s, %s)"
		student_data = [
			("angammana sumana", "Badulla", "0771234567", "angammana_sumana@anatha.com", 20),
			("samantha", "Badulla", "0774589247", "samantha@modaya.lk", 14),
			("buruwa", "Colombo", "0745269734", "buruwa@burupetiya.org", 16),
			("sara", "Galle", "0712382811", "sara@polleli.org", 22),
			("winkale", "Matara", "0721229272", "winkale@uncle.org", 13),
			("andare", "Hambantota", "0772128261", "andare@fun.org", 12),
			("viraj", "Kurunegala", "0778818182", "viraj@people.org", 15),
			("sumane", "Jaffna", "0788903789", "sumane@angammana.org", 17),
			("halapaya", "Kurunegala", "0700969734", "halapa@sumane.org", 19),
			("methuja", "Trincomalee", "0748969734", "methuja@gn.org", 18),
			("balla", "Puttalam ", "0785697347", "fssfa@anatha.org", 14),
			("netha", "Jaffna", "0700967809", "achchita@halgaranna.org", 16),
			("randika", "Hambantota", "0700978734", "randika@amijoketoyou.org", 14),
			("janaka", "Kandy", "0700890734", "balu@balla.org", 13),
			("pettidevanya", "Kurunegala", "0718491277", "pettidevanya@harakdevanya.com", 14),
			("Sathuni", "Puttalam", "0253698744", "mamaharaka@pissamu.com", 13),
			("Mohini", "Kurunegala", "0731857986", "Mohini@mohini.com", 14),
			("wanethmi", "Ratnapura", "0371212011", "wanethmi@owner.org", 17),
			("kawadiya", "Mannar", "0713029101", "kawadiya@kakusara.org", 17),
			("bantiya", "Anuradhapura", "0722211918", "bantiya@kalla.org", 16),
			("galivar", "Batticaloa", "0771902191", "galivar@asss.org", 18),
			("Red pin", "Jaffna", "0712191910", "Redpin@association.org", 22),
		]

		# data for table marks
		# :1 studentId, :2 studentName, :3 maths, :4 science, :5 ict, :6 english, :7 total, :8 average
		marks_command = "INSERT INTO marks (studentId, studentName, maths, science, ict, english, total, average) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		marks_data = [
			("angammana sumana", 80, 90, 70, 80, (80+90+70+80), (80+90+70+80)/4),
			("samantha", 70, 80, 90, 70, (70+80+90+70), (70+80+90+70)/4),
			("buruwa", 80, 70, 80, 90, (80+70+80+90), (80+70+80+90)/4),
			("sara", 70, 80, 90, 70, (70+80+90+70), (70+80+90+70)/4),
			("winkale", 80, 70, 80, 90, (80+70+80+90), (80+70+80+90)/4),
			("andare", 70, 80, 90, 70, (70+80+90+70), (70+80+90+70)/4),
			("viraj", 80, 70, 80, 90, (80+70+80+90), (80+70+80+90)/4),
			("sumane", 75, 92, 57, 70, (75+92+57+70), (75+92+57+70)/4),
			("halapaya", 86, 73, 87, 92, (86+73+87+92), (86+73+87+92)/4),
			("methuja", 78, 45, 32, 84, (78+45+32+84), (78+45+32+84)/4),
			("balla", 35, 56, 89, 92, (35+56+89+92), (35+56+89+92)/4),
			("netha", 72, 49, 56, 98, (72+49+56+98), (72+49+56+98)/4),
			("randika", 84, 65, 56, 90, (84+65+56+90), (84+65+56+90)/4),
			("janaka", 45, 65, 23, 12, (45+65+23+12), (45+65+23+12)/4),
			("pettidevanya", 85, 71, 87, 49, (85+71+87+49), (85+71+87+49)/4),
			("Sathuni", 53, 49, 80, 35, (53+49+80+35), (53+49+80+35)/4),
			("Mohini", 80, 71, 64, 94, (80+71+64+94), (80+71+64+94)/4),
			("wanethmi", 65, 58, 92, 87, (65+58+92+87), (65+58+92+87)/4),
			("kawadiya", 65, 58, 23, 15, (65+58+23+15), (65+58+23+15)/4),
			("bantiya", 65, 69, 25, 45, (65+69+25+45), (65+69+25+45)/4),
			("galivar", 88, 58, 69, 32, (88+58+69+32), (88+58+69+32)/4),
			("Red pin", 71, 88, 99, 65, (71+88+99+65), (71+88+99+65)/4),
		]

		for x, student in enumerate(student_data):
			mycursor.execute(student_cammand, student)

		for x, mark in enumerate(marks_data):
			mycursor.execute(marks_command, (x+1,) + mark)

		db.commit()

		print(f"all records are inserted to table {table_name} [+]")
		status = True
	except:
		print(f"unable to seed data to table: {table_name} in database: {db_name} [-]")
