import sqlite3

class Student():
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()

	def create_student(self,firstname,lastname,sex,birthdate,age,phone,address,Id,year,course):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = f'{self.firstname} {self.lastname}',
		self.sex = sex
		self.birthdate = birthdate
		self.age = age
		self.phone = phone
		self.address = address
		self.year = year
		self.course = course

		self.cursr.execute("INSERT INTO students (?,?,?,?,?,?,?,?,?,?,?)",(
			self.firstname,
			self.lastname,
			self.fullname,
			self.sex,
			self.birthdate,
			self.age,
			self.phone,
			self.address,
			self.year,
			self.course	
		))
		return print(f'{self.fullname} successfully created as a student...')


	def add_course(self,student,course,yr):
		student_tuple,course_tuple = (student,),(course_tuple,)
		if student_tuple not in self.cursr.execute("SELECT fullname FROM students") or course_tuple not in self.cursr.execute("SELECT name FROM courses"):
			return print('Error 404')

		# configuring objects
		course_id = f'{course}/yr-{yr}'
		course_students = self.cursr.execute("SELECT students FROM courses WHERE courseId = ?",(course_id,)).fetchone()
		cs_list = json.loads(course_students[0])

		# checking the student
		if student in cs_list or self.cursr.execute("SELECT course FROM students WHERE fullname = ?",(student,)).fetchone()[0] != None:
			return print('Student is already enrolled...')

		# updating the server
		cs_list.append(student)
		self.cursr.execute("UPDATE courses SET students = ? WHERE courseId = ?",(json.dumps(cs_list),course_id))
		self.cursr.execute("UPDATE students SET course = ? WHERE fullname =?",(course,student))

		# committing and closing
		self.cnt.commit()
		self.cnt.close()

		return print(f'{student} enrolled in {course}-{yr} successfully')



if __name__ == '__main__':
	pass

	# cnt = sqlite3.connect('school.db')
	# cursr = cnt.cursor()
	# cnt.commit()
	# cnt.close()