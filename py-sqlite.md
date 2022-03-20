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


## Get objects through table classifications and Primary key
```
cursr.execute("SELECT rowid FROM students") # see row id
cursr.execute("SELECT rowid,* FROM students") # see row id and all objects

cursr.execute("SELECT fname FROM students") # see only specific attributes
print(cursr.fetchall())
```


## Use `WHERE` for searching
```
cursr.execute("SELECT * FROM students WHERE fname = 'Kel'")

# you can search through number, exact value, or in greater/less than
cursr.execute("SELECT * FROM students WHERE age >= 15")


print(cursr.fetchall())
```
-Search similar things or objects with the same characters in the said attributes. 
Format: `cursr.execute("SELECT * FROM students WHERE att LIKE '%chars'")`
```
# cursr.execute("SELECT * FROM students WHERE fname LIKE 'ke%'") # starts%
# cursr.execute("SELECT * FROM students WHERE email LIKE '%ar%'") # %mid%
# cursr.execute("SELECT * FROM students WHERE fname LIKE '%el'") # %ends
```


## Update
-Syntax: cursr.execute("UPDATE students SET att = val WHERE att = val")
```
cursr.execute("UPDATE students SET fname = 'Maykel' WHERE rowid = 1")

cnt.commit()

# you can print it to see if it really works
cursr.execute("SELECT * FROM students")
print(cursr.fetchall())
```


## Delete
```
cursr.execute("DELETE from students WHERE rowid = 4")
```
-NOTE: When making a delete function, you should convert the id into str coz if not, it won't work
```
def delete-one(id)
	...
	cursr.execute("DELETE from students WHERE rowid = (?)", id)
	...
delete-one('2')
```


## Ordering
```
# ASC -ascending,DESC -descending,
cursr.execute("SELECT rowid,* FROM students ORDER BY fname ASC")
```


## And, Or
```
# AND -both. You do many AND; make cursr.execute(..., AND ... AND ... ) 
cursr.execute("SELECT rowid,* FROM students WHERE email LIKE '%030%' AND rowid = 3")
# OR -either, or. You do many OR; make cursr.execute(..., OR ... OR ... )
cursr.execute("SELECT rowid,* FROM students WHERE email LIKE '%030%' OR rowid = 2")
```

## Limit
```
cursr.execute("SELECT rowid,* FROM students WHERE email LIKE '%03%' OR rowid = 3 LIMIT 1")
```

## Delete a whole Table
```
cursr.execute("DROP TABLE students")
cnt.commit()
```