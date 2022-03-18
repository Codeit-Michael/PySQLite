import sqlite3

# create & connect to db
connect = sqlite3.connect('student.db')
cursr = connect.cursor()


# Create a table
# cursr.execute("""CREATE TABLE students (
# 		fname text,
# 		lname text,
# 		email text
# 	)""")


# Inserting a data in table
# connect.execute("INSERT INTO students VALUES ('Kel', 'Maranan', 'marananm030@gmail.com')")


# Inserting many data in table
the_students = [
    ('Agg','Mar','aggMar03@gmail.com'),
    ('Michael','Maranan','michaelmaranan030@gmail.com')
]
connect.executemany("INSERT INTO students VALUES (?,?,?)", the_students)


connect.commit()
connect.close()
