## create & connect to db
-To make and connect to db
```
connect = sqlite3.connect('student.db')
cursr = connect.cursor() # making cursor
```
-Run like ordinary py file, python filename.py, to create the db


## Create a table
5 SQLite Datatypes
1. NULL => None
2. INTEGER => int
3. REAL => float
4. TEXT => str
5. BLOB => files (image, files, etc.)

-To make a table
```
cursr.execute("""CREATE TABLE students (
		fname text,
		lname text,
		email text
	)""") # can done in 1 line but messy

connect.commit() # committing
connect.close() # closing connections
```
-always make sure you put `.commit()` and `.close()` on every end of your configuration

 
## Inserting one data in table
```
cursr.execute("INSERT INTO students VALUES ('Kel', 'Maranan', 'marananm030@gmail.com')")

connect.commit() # committing
connect.close() # closing connections
```
-Run it, and it's all fine


## Inserting many data in table
-We're gonna use lists
```
the_students = [
    ('Agg','Mar','aggMar03@gmail.com'),
    ('Michael','Maranan','michaelmaranan030@gmail.com')
]
cursr.executemany("INSERT INTO students VALUES (?,?,?)", the_students)

connect.commit() # committing
connect.close() # closing connections
```


## Fetch object
```
cursr.execute("SELECT * FROM students")
# print(cursr.fetchone()) # 1 object
# print(cursr.fetchmany(2)) # select given amount
print(cursr.fetchall()) # all

connect.commit() # committing
connect.close() # closing connections
```


## Format results
-Example, db has:
```
the_students = [
#     ('Agg','Mar','aggMar03@gmail.com'),
#     ('Michael','Maranan','michaelmaranan030@gmail.com')
# ]
```
-And we try to access the 1st attribute from the 1st tuple. so we do:
```
print(cursr.fetchall()[0][0])

# or maybe
studs = cursr.all()
for item in studs: print f'{studs[0]} {studs[1]} {studs[2]}'
```