import sqlite3

class Subject():
	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()

	def create_subject(self,name):
		self.name = name
		self.professor  = None
		# self.related = {} # missing
		self.cursr.execute("INSERT INTO subjects VALUES (?,?)",(self.name,self.professor))
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


if __name__ == '__main__':
	# g1 = Subject().create_subject('NSTP')
	g1 = Subject().add_professor('NSTP','Michael Maranan')

	cnt = sqlite3.connect('school.db')
	cursr = cnt.cursor()
	cursr.execute("SELECT * FROM subjects")
	print(cursr.fetchall())
	cnt.close()