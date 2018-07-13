favorite_places = {
	'arusa' : ['japan', 'south korea'],
	'subhan' : ['france', 'spain', 'australia'],
	'emily' : ['japan', 'italy', 'hawaii']
}

for name, countries in favorite_places.items():
	print("\n" + name.title() + "'s favorite places to visit are :")
	for country in countries:
		print("\t" + country.title())