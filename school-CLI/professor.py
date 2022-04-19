import sqlite3
import json
from person import Person


cnt = sqlite3.connect('school.db')
cursr = cnt.cursor()

class Professor(Person):

	def create_professor(self,firstname,lastname,sex,birthdate,age,phone,address,salary):
		super().create_person(firstname,lastname,sex,birthdate,age,phone,address)
		self.salary = salary
		self.teaching = []

		cursr.execute("INSERT INTO professors VALUES (?,?,?,?,?,?,?,?,?,?)",(
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
		cnt.commit()
		cnt.close()
		return print(f'{self.firstname} successfully created as a professor...')


	def add_teaching(self,subject,professor):
		# configuring objects
		professor_subjects = cursr.execute("SELECT teaching FROM professors WHERE fullname = ?",(professor,))
		professor_subjects = professor_subjects.fetchall()
		self.teaching = json.loads(professor_subjects[0][0])
		subject_list =  cursr.execute("SELECT name FROM subjects").fetchall()
		subject_tuple = (subject,)

		# adding subject in Professor's teachings
		if subject_tuple not in subject_list or subject in self.teaching:
			return print('Subject doesn\'t exist or the Professor has the subject already')
		self.teaching.append(subject)
		cursr.execute("UPDATE professors SET teaching = ? WHERE fullname = ?",(json.dumps(self.teaching),professor))
		
		# adding Professor on the said project
		if cursr.execute("SELECT name FROM subjects WHERE professor = ?",(professor,)).fetchone()[0] != None:
			return print(f'{subject} has teacher already assigned')
		cursr.execute("UPDATE subjects SET professor = ? WHERE name = ?",(professor,subject))
		
		cnt.commit()
		cnt.close()
		print(f'Added {subject} into {professor}\'s teachings')


	def get_salary(self,professor):
		subjects = cursr.execute("SELECT teaching FROM professors WHERE fullname = ?",(professor,))
		subjects = subjects.fetchone()
		subject_list = json.loads(subjects[0])
		salary = 5000 * len(subject_list)
		return salary


	def view_professors(self):
		professor_table = cursr.execute("SELECT * FROM professors")
		professor_table = professor_table.fetchall()
		cnt.close()
		return print(professor_table)


if __name__ == "__main__":
	hello = Professor().create_professor('Kel','Mar','male','09/14/03',18,'09162667676','Maymangga,Cavite',0.0)
	# hello = Professor().view_professors()
	# print(hello)