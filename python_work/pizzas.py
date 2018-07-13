pizzas = ['veggie', 'supreme', 'chicago', 'new york']
friends_pizza = pizzas[:]

pizzas.append('detroit')
friends_pizza.append('italian')

for pizza in pizzas:
	print("I like " + pizza.title() + " pizza.\n")

for pizza in friends_pizza:
	print("My friend likes " + pizza.title() + " pizza.\n")

print("Pizza is my favorite food!\n")

electric_pokemon = ['pikachu', 'electrike', 'jolteon', 'mareep']
electric_pokemon.append('elekid')

for pokemon in electric_pokemon:
	print(pokemon.title() + " is a cute electric pokemon.\n")

print("All eletric pokemon are amazing!")