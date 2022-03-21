from person import Person
# from course import Course
import sqlite3

cnt = sqlite3.connect('school.db')
cursr = cnt.cursor()

cursr.execute("""CREATE TABLE students (
	firstname text,
	lastname text ,
	birthdate text,
	age integer,
	phone text,
	address text
	Id text,
	year integer,
	course text
)""")

cnt.commit()
cnt.close()


class Student():
	def __init__(self,firstname,lastname,birthdate,age,phone,address,Id):
		super().__init__(self,firstname,lastname,birthdate,age,phone,address)
		self.Id = Id
		
		# missing
		self.year = None
		# self.on_probation = False
		self.course = None

