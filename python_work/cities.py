the_cities = {
	'greensboro': {
		'location' : 'nc',
		'population' : 300000,
		'fact' : 'it is green'
	},

	'new york' : {
		'location' : 'ny',
		'population' : 1000000,
		'fact' : 'it is the biggest city in america',
	},

	'chicago' :{
		'location' : 'il',
		'population' : 1000000,
		'fact' : 'it is the windy city of america',
	}
}

for city, city_info in the_cities.items():
	print("\nCity: " + city)
	city_location = city_info['location']
	city_population = city_info['population']
	city_fact = city_info['fact']

	print("\tThe city is located in " + city_location.upper())
	print("\tThe cities population is " + str(city_population))
	print("\tA fact about this city is " + city_fact)