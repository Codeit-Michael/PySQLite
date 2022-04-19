import sqlite3
import json


cnt = sqlite3.connect('school.db')
cursr = cnt.cursor()

class Subject():

	def create_subject(self,name):
		self.name = name
		self.professor  = None
		self.related = []

		cursr.execute("INSERT INTO subjects VALUES (?,?,?)",(
			self.name,
			self.professor,
			json.dumps(self.related)
		))
		cnt.commit()
		cnt.close()


	def fetch_professor_subjects(self,professor):
		professor_subjects = cursr.execute("SELECT teaching FROM professors WHERE fullname = ?",(professor,))
		professor_subjects = professor_subjects.fetchone()
		teaching = json.loads(professor_subjects[0])
		return teaching


	def check_subject_existance(self,subject,teaching_list):
		subject_prof = cursr.execute("SELECT professor FROM subjects WHERE name = ?",(subject,)).fetchone()[0]
		if subject_prof != None:
			return print(f'{Subject} has professor already assigned')
		if subject in teaching_list:
			return print('Professor has the subject already')


	def add_professor(self,professor,subject):
		self.teaching = self.fetch_professor_subjects(professor)
		self.check_subject_existance(subject,self.teaching)
		self.teaching.append(subject)
		cursr.execute("UPDATE professors SET teaching = ? WHERE fullname = ?",(json.dumps(self.teaching),professor))
		cursr.execute("UPDATE subjects SET professor = ? WHERE name = ?",(professor,subject))
		cnt.commit()
		cnt.close()
		return print(f'Added {subject} into {professor}\'s teachings')


	def add_related(self,subject,course,yr):
		course_tuple,subject_tuple = (subject,),(course,)
		if subject_tuple not in cursr.execute("SELECT name FROM subjects") or course_tuple not in cursr.execute("SELECT name FROM courses"):
			return print('Subject and/or Course not found...')

		# configuring objects
		course_id = f'{subject}/yr-{yr}'
		course_related = cursr.execute("SELECT related FROM subjects WHERE courseId = ?",(course_id,)).fetchone()
		course_subjects = cursr.execute("SELECT subjects FROM courses WHERE name = ?",(subject,)).fetchone()
		cr_list = json.loads(course_related[0])
		cs_list = json.loads(course_subjects[0])

		# adding course and subject to their lists
		if course in cr_list or subject in cs_list:
			return print('Course has Subject already or Subject in Course already')
		cr_list.append(course)
		cs_list.append(subject)

		# updating the server
		cursr.execute("UPDATE subjects SET related = ? WHERE name = ?",(cr_list,subject))
		cursr.execute("UPDATE courses SET subjects = ? WHERE courseId = ?",(cs_list,course_id))

		# saving and closing
		cnt.commit()
		cnt.close()

		return print(f'{subject} added in {course}-{yr} successfully')


if __name__ == "__main__":
	# hello = Subject().create_subject('Art Appreciation')