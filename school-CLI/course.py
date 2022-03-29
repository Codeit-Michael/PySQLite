import sqlite3
import json

class Course():
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()

	def create_course(self,name,for_year):
		self.name = name
		self.for_year = for_year
		self.courseId = f'{name}/yr-{for_year}'
		self.students = []
		self.subjects = []

		self.cursr.execute("INSERT INTO courses VALUES (?,?,?,?,?)",(
			self.name,
			self.for_year,
			self.courseId,
			json.dumps(self.students),
			json.dumps(self.subjects)
		))


	def add_subjects(self,subject,course,yr):
		course_tuple,subject_tuple = (subject,),(course,)
		if subject_tuple not in self.cursr.execute("SELECT name FROM subjects") or course_tuple not in self.cursr.execute("SELECT name FROM courses"):
			return print('Subject and/or Course not found...')

		# configuring objects
		course_id = f'{subject}/yr-{yr}'
		course_related = self.cursr.execute("SELECT related FROM subjects WHERE courseId = ?",(course_id,)).fetchone()
		course_subjects = self.cursr.execute("SELECT subjects FROM courses WHERE name = ?",(subject,)).fetchone()
		cr_list = json.loads(course_related[0])
		cs_list = json.loads(course_subjects[0])

		# adding course and subject to their lists
		if course in cr_list or subject in cs_list:
			return print('Course has Subject already or Subject in Course already')
		cr_list.append(course)
		cs_list.append(subject)

		# updating the server
		self.cursr.execute("UPDATE subjects SET related = ? WHERE name = ?",(json.dumps(cr_list),subject))
		self.cursr.execute("UPDATE courses SET subjects = ? WHERE courseId = ?",(json.dumps(cs_list),course_id))

		# saving and closing
		self.cnt.commit()
		self.cnt.close()

		return print(f'{subject} added in {course}-{yr} successfully')


if __name__ == '__main__':
	pass