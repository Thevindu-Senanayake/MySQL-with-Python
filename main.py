import create_db
import check_connection
import create_tables
import seed_data
import filter_first_ten_records as first_ten
import update_records as update
import filter_records_by_location as location
import delete_students
import sort_students

# check that mysql server is running and can make a connection to it
check_connection.check_connection()

# create database for project
if check_connection.status:
	create_db.createDb()
else:
	exit()

# create two tables student and marks
if create_db.status:
	create_tables.create_tables()
else:
	exit()

# add records to tables
if create_tables.status:
	seed_data.seed_data()
else:
	exit()

# find first ten student with highest marks
if seed_data.status:
	first_ten.filter()

# update first five students
if first_ten.status:
	update.update_records()

# find students with same location
if update.status:
	location.filter()

# delete student that has marks less than 40
if location.status:
	delete_students.delete()

# sort student and marks tables by name in ascending order
if delete_students.status:
	sort_students.sort()