

def show_magicians(magicians):

	for name in magicians:
		msg = ("Hello, " + name.title() + ", thank you for coming!")
		print(msg)

def make_great(magicians):

	great_magicians = []

	while magicians:
		current_magician = magicians.pop()

		new_magician = current_magician.title() + " The Great"

		great_magicians.append(new_magician)

	for great_magician in great_magicians:
		magicians.append(great_magician)

	return magicians




magicians = ['houdini', 'chris angel', 'david blaine']
show_magicians(magicians)


print("\nThe great magicians: ")
the_great = make_great(magicians[:])
show_magicians(the_great)

print("\nThe original ones: ")
show_magicians(magicians)




