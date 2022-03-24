import sqlite3
import json

class Subject():
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()


	def create_subject(self,name):
		self.name = name
		self.professor  = None
		self.related = []

		self.cursr.execute("INSERT INTO subjects VALUES (?,?)",(
			self.name,
			self.professor,
			json.dumps(self.related)
		))
		self.cnt.commit()
		self.cnt.close()


	def add_professor(self,subject,professor):
		prof = self.cursr.execute("SELECT fullname FROM professors WHERE fullname = ?",(professor,))
		
		if len(prof.fetchall()) == 0:
			return print(f'Prof.\'{professor}\' not found...')
		
		elif self.cursr.execute("SELECT professor FROM subjects WHERE name = ?",(subject,)) != None:
			return print('Subject has professor already...')
		
		self.cursr.execute("UPDATE subjects SET professor = ? WHERE name = ?",(professor,subject))
		print(f'Subject added to Prof.{professor}\'s teachings')
		self.cnt.commit()
		self.cnt.close()


	def add_related(self,subject,course,yr):
		course_id = f'{subject}/yr-{yr}'
		related = self.cursr.execute("SELECT name FROM courses WHERE courseId = ?",(course_id,))
		
		if len(related.fetchall()) == 0:
			return print(f'\'{course}-{yr}\' not found...')
		
		related = self.cursr.execute("SELECT related FROM subjects WHERE name = ?",(subject,))
		self.related = json.loads(related[0][0])
		if subject in self.related:
			return print('Subject already into the course')
		
		self.related.append(subject)
		self.cursr.execute("UPDATE subjects SET related = ? WHERE name = ?",(json.loads(self.add_related),subject))
		print(f'{course}-{yr} now has {subject}')
		self.cnt.commit()
		self.cnt.close()		


if __name__ == '__main__':
	pass
	# g1 = Subject().create_subject('NSTP')
	# g1 = Subject().add_professor('NSTP','Michael Maranan')

	# cnt = sqlite3.connect('school.db')
	# cursr = cnt.cursor()
	# cursr.execute("SELECT * FROM subjects")
	# print(cursr.fetchall())
	# cnt.commit()
	# cnt.close()