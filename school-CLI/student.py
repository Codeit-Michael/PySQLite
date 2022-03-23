from person import Person
# from course import Course
import sqlite3

class Student():
	def __init__(self,firstname,lastname,sex,birthdate,age,phone,address,Id):
		super().__init__(firstname,lastname,fullname,sex,birthdate,age,phone,address)
		self.Id = Id
		
		# missing
		self.year = None
		# self.on_probation = False
		self.course = None

