sandwhich_orders = ['tuna salad', 'pastrami', 'ham', 'pastrami', 'roast beef', 'italian', 'pastrami']
finished_sandwhich = []

print("\nSorry we are out of pastrami")

while 'pastrami' in sandwhich_orders:
	sandwhich_orders.remove('pastrami')

while sandwhich_orders:
	current_sandwich = sandwhich_orders.pop()

	print("\nThe " + current_sandwich.title() + " is being made")

	finished_sandwhich.append(current_sandwich)

print("\nThe following sandwhiches has been made: ")
for finish_sandwhich in finished_sandwhich:
	print(finish_sandwhich.title())