import sqlite3
import json

class Professor:
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()


	def create_professor(self,firstname,lastname,sex,birthdate,age,phone,address,salary):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = f'{self.firstname} {self.lastname}'
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
		self.cnt.close()
		return print(f'{self.firstname} successfully created as a professor...')


	def add_teaching(self,subject,professor):
		self.cursr.execute("SELECT teaching FROM professors WHERE fullname = ?",(professor,))
		subjects = self.cursr.fetchall()
		self.teaching = json.loads(subjects[0][0])

		subject_list =  self.cursr.execute("SELECT name FROM subjects")
		subject_tuple = (subject,)
		if subject_tuple not in subject_list.fetchall() or subject in self.teaching:
			return print('Subject doesn\'t exist or the Professor has the subject already')

		self.teaching.append(subject)
		self.cursr.execute("UPDATE professors SET teaching = ? WHERE fullname = ?",(json.dumps(self.teaching),professor))
		
		if self.cursr.execute("SELECT name FROM subjects WHERE professor = ?",(professor,)) != None:
			return print(f'{subject} has teacher already assigned')

		self.cursr.execute("UPDATE subjects SET professor = ? WHERE name = ?",(professor,subject))
		self.cnt.commit()
		self.cnt.close()
		print(f'Added {subject} into {professor}\'s teachings')


if __name__ == "__main__":
	# p1 = Professor().create_professor('Kevin','Belingon','male','08/15/93',28,'09162596988','Bucal,Cavite',30500.05)
	# p1 = Professor().add_teaching('NSTP','Michael Maranan')

	# cnt = sqlite3.connect('school.db')
	# cursr = cnt.cursor()
	# cursr.execute("SELECT * FROM professors")
	# print(cursr.fetchall())
	# cnt.commit()
	# cnt.close()
