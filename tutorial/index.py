import sqlite3
import json

class hola():
	cnt = sqlite3.connect('student.db')
	cursr = cnt.cursor()

	def create(self,name):
		self.name = name
		self.randm = []
		self.randm = json.dumps(self.randm)

		self.cursr.execute("INSERT INTO persons VALUES (?,?)",(self.name,self.randm))
		self.cnt.commit()

	def add_randm(self,txt,my_id):
		self.cursr.execute("SELECT randm FROM persons WHERE rowid = (?)",str(my_id))
		new = self.cursr.fetchall()
		self.randm = json.loads(new[0][0])
		print(type(self.randm))


if __name__ == '__main__':
	p1 = hola()
	p1.add_randm('hello',3)


	cnt = sqlite3.connect('student.db')
	cursr = cnt.cursor()
	cursr.execute("DROP TABLE persons")
	# cursr.execute("select * from persons")
	# cursr.execute("select * from persons where rowid = (?)",('1'))
	# print(cursr.fetchall())

	cnt.commit()
	cnt.close()