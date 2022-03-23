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

	def add_student(self,student,course,yr):
		course_id = f'{course}/yr-{yr}'
		self.cursr.execute("SELECT students FROM courses WHERE name = ?",(course,))
		students = self.cursr.fetchall()
		self.students = json.loads(students[0][0])
		self.students.append(student)
		self.cursr.execute("UPDATE courses SET students = ? WHERE courseId = ?",(json.dumps(self.students),course_id))
		self.cnt.commit()
		print(f'{student} enrolled in {course}-{yr}')


if __name__ == '__main__':
	pass