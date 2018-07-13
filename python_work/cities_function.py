def cities(city, country = 'italy'):
	"""Displays where a city is located in what country"""
	print(city.title() + " is located in " + country.title())

cities('rome')
cities(city='naples')
cities(city='osaka',country = 'japan')
