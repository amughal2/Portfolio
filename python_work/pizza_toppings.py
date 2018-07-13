prompt = "\nPlease enter the kinds of toppings you would like to have on your pizza: "
prompt += "\n(Enter 'quit' when you have enough toppings) "





while True:

	toppings = input(prompt)

	if toppings == 'quit':
		 break

	else:
		print("Adding the " + toppings + " to the pizza now!")
