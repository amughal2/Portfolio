class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):

		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("This Restaurant is called the " + self.restaurant_name.title())
		print("\n" + self.restaurant_name.title() + " serves " + self.cuisine_type + " food\n")

	def open_restaurant(self):
		print("\nThe " + self.restaurant_name.title() + " is currently open")

	def read_served(self):
		print("This restaurant is currently serving " + str(self.number_served) + " today.")

	def update_amount_served(self, people_served):
		self.number_served = people_served


class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):

		super().__init__(restaurant_name,cuisine_type)
		

	def icecream_flavors(self, flavors):

		self.flavors = []

		for flavor in flavors:
			print("\nWe serve " + flavor)


my_icecream = IceCreamStand('cold stone', 'ice cream')
my_icecream.describe_restaurant()
flavor_type = ['vanilla', 'chocolate', 'mint', 'pistachio']
my_icecream.icecream_flavors(flavor_type)


"""my_restaurant = Restaurant('cugino', 'italian')

my_restaurant.describe_restaurant()

my_restaurant.update_amount_served(3)

my_restaurant.read_served()

my_2nd_restaurant = Restaurant('ichiban', 'japanese')

my_2nd_restaurant.describe_restaurant()

my_3rd_restaurant = Restaurant('ground zero', 'burger grill')

my_3rd_restaurant.describe_restaurant()"""