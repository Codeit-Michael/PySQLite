import sqlite3

# create & connect to db
connect = sqlite3.connect('student.db') # run like ordinary py file, python filename.py, to create the db
cursr = connect.cursor() # create a cursor


# Create a table
cursr.execute("""CREATE TABLE students (
		fname text,
		lname text,
		email text
	)""") # can done in 1 line but messy
"""
5 SQLite Datatypes
 NULL => None
 INTEGER => int
 REAL => float
 TEXT => str
 BLOB => files (image)
"""
connect.commit() # committing
connect.close() # closing connections


# Insert one into record table 
