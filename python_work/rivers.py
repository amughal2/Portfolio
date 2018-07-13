major_rivers = {
'egypt': 'nile',
 'peru': 'amazon',
 'china': 'yellow',
 }

for country, river in major_rivers.items():
 	print("The " + river.title() + " river is located in " + 
 	country.title())

for country in major_rivers.keys():
	print(country.title())

for river in major_rivers.values():
	print(river.title())