cars = ['bmw', 'audi', 'toyota', 'subaru']

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


super_car = "Mclaren"

print(super_car.lower() == "mclaren")

marth_attack = 38
ike_attack = 44
lucina_attack = 42

print("\n Are all the characters attack over 40? ")
print(marth_attack >= 40 and ike_attack >= 40 and lucina_attack >= 40)

print("\n Is atleast one character attack over 40? ") 
print( marth_attack >= 40 or ike_attack >= 40 or lucina_attack >= 40)

fire_emblem = ['roy', 'ike', 'lyn', 'hector']

emblem_warrios = ['lucina', 'marth', 'robin']

for warrios in emblem_warrios:
	if emblem_warrios not in fire_emblem:
		print("\n" + warrios.title() + " would you like to join the cast?")

for cast in fire_emblem:
	if cast in fire_emblem:
		print("\n" + cast.title() + " do you want to remain in the cast?")








