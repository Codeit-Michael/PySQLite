class Person():
	def __init__(self,firstname,lastname,birthdate,age,phone,address):
		self.firstname = firstname
		self.lastname = lastname
		self.birthdate = birthdate
		self.age = age
		self.phone = phone
		self.address = address
		self.fullname = f'{self.firstname} {self.lastname}'

	def __repr__(self):
		return self.fullname