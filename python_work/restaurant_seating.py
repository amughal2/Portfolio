number_of_seats = input("Please enter the amount of people in your dinner group : ")
number_of_seats = int(number_of_seats)

if number_of_seats > 8:
	print("I apologize but due to the size of your group you will have to wait for the next available table")
else:
	print("Your table is ready sir/madam")