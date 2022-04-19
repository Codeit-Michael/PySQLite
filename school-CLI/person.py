class Person():

	def create_person(self,firstname,lastname,sex,birthdate,age,phone,address):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = f'{self.firstname} {self.lastname}'
		self.sex = sex
		self.birthdate = birthdate
		self.age = age
		self.phone = phone
		self.address = address