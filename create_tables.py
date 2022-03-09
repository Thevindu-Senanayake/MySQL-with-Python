import mysql.connector

db_name = "anathaDb"

student_table = marks_table = False

def crete_student_table():
	global student_table
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()

		table_name = "student"

		mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(75), district VARCHAR(50), phone VARCHAR(15), email VARCHAR(50), age INT)")
		print(f"Table: {table_name} created in database: {db_name} [+]")
		student_table = True
	except:
		print(f"unable to create table: {table_name} in database: {db_name} [-]")

def crete_marks_table():
	global marks_table
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="",
			database=db_name
		)

		mycursor = db.cursor()

		table_name = "marks"

		mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (studentId INT PRIMARY KEY, studentName VARCHAR(75), maths INT DEFAULT 0, science INT DEFAULT 0, ict INT DEFAULT 0, english INT DEFAULT 0, total INT DEFAULT 0, average FLOAT)")
		print(f"Table: {table_name} created in database: {db_name} [+]")
		marks_table = True
	except Exception as e:
		print(e)
		print(f"unable to create table: {table_name} in database: {db_name} [-]")

def create_tables():
	crete_student_table()
	crete_marks_table()

def status():
	return student_table and marks_table
