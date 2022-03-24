# SCHOOL.DB TABLES #
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# cnt = sqlite3.connect('school.db')
# cursr = cnt.cursor()
# cursr.execute("DROP TABLE professors")
# cnt.commit
# cursr.execute("""CREATE TABLE professors (
# 	firstname text,
# 	lastname text ,
# 	fullname text,
# 	sex text,
# 	birthdate text,
# 	age integer,
# 	phone text,
# 	address text,
# 	salary real,
# 	teaching null
# )""")

# cnt.commit()
# cnt.close()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# cnt = sqlite3.connect('school.db')
# cursr = cnt.cursor()
# cursr.execute("""CREATE TABLE subjects (
# 	name text,
# 	professor null,
# 	related null
# )""")
# cnt.commit()
# cnt.close()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# cnt = sqlite3.connect('school.db')
# cursr = cnt.cursor()

# cursr.execute("""CREATE TABLE courses (
# 	name text,
# 	for_year integer,
# 	courseId text,
# 	students text,
# 	subjects text
# )""")

# cnt.commit()
# cnt.close()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
# cnt = sqlite3.connect('school.db')
# cursr = cnt.cursor()

# cursr.execute("""CREATE TABLE students (
# 	firstname text,
# 	lastname text ,
# 	fullname text,
# 	sex text,
# 	birthdate text,
# 	age integer,
# 	phone text,
# 	address text,
# 	Id text,
# 	year integer,
# 	course text
# )""")

# cnt.commit()
# cnt.close()
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
