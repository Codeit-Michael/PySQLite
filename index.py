import sqlite3

# create & connect to db
cnt = sqlite3.connect('student.db')
cursr = cnt.cursor()


# Create a table
# cursr.execute("""CREATE TABLE students (
# 		fname text,
# 		lname text,
# 		email text
# 	)""")


# Inserting a data in table
# cursr.execute("INSERT INTO students VALUES ('Kel', 'Maranan', 'marananm030@gmail.com')")


# Inserting many data in table
# the_students = [
#     ('Agg','Mar','aggMar03@gmail.com'),
#     ('Michael','Maranan','michaelmaranan030@gmail.com')
# ]
# cursr.executemany("INSERT INTO students VALUES (?,?,?)", the_students)


# # Fetch/Show objects
# cursr.execute("SELECT * FROM students")
# print(cursr.fetchall())


cnt.commit()
cnt.close()
