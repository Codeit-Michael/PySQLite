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
		subject_tuple, professor_tuple = (subject,), (professor,)
		if subject_tuple not in self.cursr.execute("SELECT name FROM subjects") or professor_tuple not in self.cursr.execute("SELECT fullname IN professors"):
			return print('SUbject and/or Professor not found...')

		# configuring objects
		professor_teachings = self.cursr.execute("SELECT teaching FROM professors WHERE fullname = ?",(professor,)).fetchone()
		pt_list = json.loads(professor_teachings[0])

		# looking if the subject has professor already
		if self.cursr.execute("SELECT professor FROM subjects WHERE name = ?",(subject,)).fetchone()[0] != None:
			return print('Subject has professor already...')
		
		# updating the server
		self.cursr.execute("UPDATE subjects SET professor = ? WHERE name = ?",(professor,subject))
		self.cursr.execute("UPDATE professors SET teaching = ? WHERE fullname = ?",(json.dumps(pt_list),professor))

		# saving and closing
		self.cnt.commit()
		self.cnt.close()

		print(f'Subject added to Prof.{professor}\'s teachings')


	def add_related(self,subject,course,yr):
		course_tuple,subject_tuple = (subject,),(course,)
		if subject_tuple not in self.cursr.execute("SELECT name FROM subjects") or course_tuple not in self.cursr.execute("SELECT name FROM courses"):
			return print('Subject and/or Course not found...')

		# configuring objects
		course_id = f'{subject}/yr-{yr}'
		course_related = self.cursr.execute("SELECT related FROM subjects WHERE courseId = ?",(course_id,)).fetchone()
		course_subjects = self.cursr.execute("SELECT subjects FROM courses WHERE name = ?",(subject,)).fetchone()
		cr_list = json.loads(course_related[0])
		cs_list = json.loads(course_subjects[0])

		# adding course and subject to their lists
		if course in cr_list or subject in cs_list:
			return print('Course has Subject already or Subject in Course already')
		cr_list.append(course)
		cs_list.append(subject)

		# updating the server
		self.cursr.execute("UPDATE subjects SET related = ? WHERE name = ?",(cr_list,subject))
		self.cursr.execute("UPDATE courses SET subjects = ? WHERE courseId = ?",(cs_list,course_id))

		# saving and closing
		self.cnt.commit()
		self.cnt.close()

		return print(f'{subject} added in {course}-{yr} successfully')


if __name__ == '__main__':
	pass