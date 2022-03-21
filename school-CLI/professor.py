from person import Person
# from subject import Subject
import sqlite3

cnt = sqlite3.connect('school.db')
cursr = cnt.cursor()

cursr.execute("""CREATE TABLE professor (
	firstname text,
	lastname text ,
	birthdate text,
	age integer,
	phone text,
	address text,
	salary real
)""")


cnt.commit()
cnt.close()


class Professor(Person):
	def __init__(self,firstname,lastname,birthdate,age,phone,address,salary):
		super().__init__(self,firstname,lastname,birthdate,age,phone,address)
		self.salary = salary

		# missing
		self.teaching = []
