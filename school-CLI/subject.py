import sqlite3

class Subject():
	def __init__(self,name,professor):
		self.name = name
		self.professor = professor
		# missing
		self.related = {}
