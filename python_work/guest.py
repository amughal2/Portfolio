guest_name = input("Please enter your name so we can enter in in a text file ")
guestfile = 'guests.txt'


with open(guestfile, 'w') as guest_object:
	
	
	guest_object.write(guest_name)