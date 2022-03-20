import sqlite3

# # Create & connect to db
cnt = sqlite3.connect('student.db')
cursr = cnt.cursor()


# # Create a table
# cursr.execute("""CREATE TABLE students (
# 		fname text,
# 		lname text,
# 		email text
# 	)""")


# # Inserting a data in table
# cursr.execute("INSERT INTO students VALUES ('Kel', 'Maranan', 'marananm030@gmail.com')")


# # Inserting many data in table
# the_students = [
#     ('Agg','Mar','aggMar03@gmail.com'),
#     ('Michael','Maranan','michaelmaranan030@gmail.com')
# ]
# cursr.executemany("INSERT INTO students VALUES (?,?,?)", the_students)

# # Fetch/Show objects and Row Ids
# cursr.execute("SELECT rowid,fname FROM students")
# print(cursr.fetchall())


# # Use WHERE for searching
# cursr.execute("SELECT * FROM students WHERE fname LIKE '%el'") # %ends
# print(cursr.fetchall())


# # Update
# cursr.execute("UPDATE students SET fname = 'Maykel' WHERE rowid = 1")


# # Delete
# cursr.execute("DELETE from students WHERE rowid = 4")


# # Order by
# cursr.execute("SELECT rowid,* FROM students ORDER BY fname ASC")
# print(cursr.fetchall())


# # And, Or
# cursr.execute("SELECT rowid,* FROM students WHERE email LIKE '%030%' AND rowid = 3")
# cursr.execute("SELECT rowid,* FROM students WHERE email LIKE '%030%' OR rowid = 2")
# print(cursr.fetchall())


# # Limit
# cursr.execute("SELECT rowid,* FROM students WHERE email LIKE '%03%' OR rowid = 3 LIMIT 1")


# # Delete a whole table
# cursr.execute("DROP TABLE students")
# cnt.commit()


cnt.commit()
cnt.close()
