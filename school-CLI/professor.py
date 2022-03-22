# from person import Person
import sqlite3
import json

class Professor:
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()

	def create_professor(self,firstname,lastname,birthdate,age,phone,address,salary):
		self.firstname = firstname
		self.lastname = lastname
		self.birthdate = birthdate
		self.fullname = f'{self.firstname} {self.lastname}'
		self.age = age
		self.phone = phone
		self.address = address
		self.salary = salary
		self.teaching = []

		self.cursr.execute("INSERT INTO professors VALUES (?,?,?,?,?,?,?,?)",(
			self.firstname,
			self.lastname,
			self.birthdate,
			self.age,
			self.phone,
			self.address,
			self.salary,
			json.dumps(self.teaching)
		))
		self.cnt.commit()


	def add_teaching(self,subject,fname,lname):
		self.cursr.execute("SELECT teaching FROM professors WHERE firstname = (?) AND lastname = (?)",(fname,lname))
		subjects = self.cursr.fetchall()
		self.teaching = json.loads(subjects[0][0])
		self.teaching.append(subject)
		self.cursr.execute("UPDATE professors SET teaching = (?) WHERE firstname = (?) AND lastname = (?)",(json.dumps(self.teaching),fname,lname))
		self.cnt.commit()
		print(f'Added {subject} into teachings')


if __name__ == "__main__":
	# mike = Professor('Michael','Maranan','09/14/03',18,'09162596988','Amadeo,Cavite',35000.05)
	mike = Professor().add_teaching('HEI','Michael','Maranan')

	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()
	cursr.execute("SELECT * FROM professors")
	print(cursr.fetchall())