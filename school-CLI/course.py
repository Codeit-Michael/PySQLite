import sqlite3

class Course():
	def __init__(self,name,for_year):
		self.name = name
		self.for_year = for_year

		# missing
		self.courseId = f'{name}{for_year}'
		self.students = []
		self.student_count = len(students)
		self.professor = None
		self.subjects = []

	def __repr__(self):
		return self.courseId

