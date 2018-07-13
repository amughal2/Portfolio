class User():

	def __init__(self, first_name, last_name, age, user_name, phone_number):

		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.user_name = user_name
		self.phone_number = phone_number
		self.login_attempts = 0

	def describe_user(self):
		print("Here is a list of the user " + self.user_name.title() + " attributes: ")
		print("\nFirst name: " + self.first_name.title())
		print("Last name: " + self.last_name.title())
		print("Age: " + str(self.age))
		print("Phone number: " + str(self.phone_number))

	def greet_user(self):
		print("\nHello " + self.user_name.title() + " I hope your having a good day!\n")

	def read_login_attempts(self):
		print("The amount of login attempts are " + str(self.login_attempts))

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0



first_user = User('emily', 'lamm', 22, 'lambchopsflowers', 9104102708)

first_user.describe_user()

first_user.greet_user()

first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()
first_user.increment_login_attempts()


first_user.read_login_attempts()

first_user.reset_login_attempts()

first_user.read_login_attempts()
"""second_user = User('subhan', 'mughal', 14, 'buttlord', 336519010)

second_user.describe_user()

second_user.greet_user()"""