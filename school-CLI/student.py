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
		course_id = f'{course}/yr-{yr}'
		course_tuple = (self.course,)

		if course_tuple not in self.cursr.execute("SELECT name FROM courses"):
			return print('Error 404')

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

		# configuring objects
		course_students = self.cursr.execute("SELECT students FROM courses WHERE courseId = ?",(course_id,)).fetchone()
		cs_list = json.loads(course_students[0])

		# updating the server
		cs_list.append(student)
		self.cursr.execute("UPDATE courses SET students = ? WHERE courseId = ?",(json.dumps(cs_list),course_id))

		self.cnt.commit()
		self.cnt.close()
		
		return print(f'{self.fullname} successfully created as a student...')


if __name__ == '__main__':
	s1 = Student().create_student('Michael', )