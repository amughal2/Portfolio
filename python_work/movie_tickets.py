prompt = "\nPlease enter your age so we can give you your ticket price: "
prompt += "\n(Enter 'quit' when you have your prices) "

active = True
while active:
	age = input(prompt)

	if age == 'quit':
		active = False

	elif int(age) <= 3:
		print("Your ticket price is 0 dollars")
	elif int(age) <= 12:
		print("Your ticket price is 10 dollars")
	else:
		print("Your ticket price is 15 follars")