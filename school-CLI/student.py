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
		self.Id = Id
		self.year = year
		self.course = course

		self.cursr.execute("INSERT INTO students (?,?,?,?,?,?,?,?,?,?,?)",(
			self.firstname,
			self.lastname,
			self.fullname
			self.sex,
			self.birthdate,
			self.age,
			self.phone,
			self.address,
			self.Id,
			self.year,
			self.course	
		))
		return print(f'{self.fullname} successfully created as a student...')

	def add_


if __name__ == '__main__':
	pass