import sqlite3
import json

class Professor:
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()

	def create_professor(self,firstname,lastname,sex,birthdate,age,phone,address,salary):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = f'{self.firstname} {self.lastname}',
		self.sex = sex
		self.birthdate = birthdate
		self.age = age
		self.phone = phone
		self.address = address
		self.salary = salary
		self.teaching = []

		self.cursr.execute("INSERT INTO professors VALUES (?,?,?,?,?,?,?,?,?,?)",(
			self.firstname,
			self.lastname,
			self.fullname,
			self.sex,
			self.birthdate,
			self.age,
			self.phone,
			self.address,
			self.salary,
			json.dumps(self.teaching)
		))
		self.cnt.commit()
		return print(f'Professor {self.firstname} successfully created as a professor...')

	def add_teaching(self,subject,professor):
		self.cursr.execute("SELECT teaching FROM professors WHERE fullname = ?",(professor,))
		subjects = self.cursr.fetchall()
		self.teaching = json.loads(subjects[0][0])
		self.teaching.append(subject)
		self.cursr.execute("UPDATE professors SET teaching = ? WHERE fullname = ?",(json.dumps(self.teaching),professor))
		self.cnt.commit()
		print(f'Added {subject} into {professor}\'s teachings')


if __name__ == "__main__":
	pass
	# p1 = Professor().create_professor('Michael','Maranan','male','09/14/03',18,'09162596988','Amadeo,Cavite',35000.05)
	# p1 = Professor().add_teaching('NSTP','Michael Maranan')

	# cnt = sqlite3.connect('school.db')
	# cursr = cnt.cursor()
	# cursr.execute("SELECT * FROM professors")
	# print(cursr.fetchall())
	# cnt.commit()
	# cnt.close()
