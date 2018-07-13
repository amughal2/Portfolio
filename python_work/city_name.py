def cities (city_name, country_name):
	full_location = city_name + ", " + country_name

	return full_location.title()

the_town = cities('paris', 'france')

print(the_town)