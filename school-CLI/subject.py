# from professor import Professor
# from course import Course
import sqlite3

cnt = sqlite3.connect('school.db')
cursr = cnt.cursor()

cursr.execute("""CREATE TABLE subjects (
	name text
)""")

cnt.commit()
cnt.close()


class Subject():
	def __init__(self,name):
		self.name = name

		# missing
		self.related = {}
		self.professor = None

	# def add_professor(self,professor):
	# 	if self.professor not None:
	# 		if not isinstance(professor, Professor):
	# 			raise Error('No teachuh named like dat shi')
	# 		self.professor = professor

	# def add_related(self,courseId):
	# 	if not isinstance(courseId, Course):
	# 		raise Error('No course-Id like that')
	# 	course,year = courseId.split('-')
	# 	self.related[course]:year