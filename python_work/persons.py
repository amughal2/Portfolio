#person_0 = {'first_name': 'emily', 'last_name': 'lamm', 'age':21, 'city': 'southern pines'}

#print(person_0)


favorite_numbers = {
	'emily': [8, 5, 77],
	'subhan': [4, 88, 101],
	'arusa':[11, 23, 44],
}

#for name in sorted(favorite_numbers.keys()):
#	print(name.title() + ", thanks for nothing losers!")

family = ['subhan', 'arusa', 'adil', 'albert']
for name in family:

	if name in favorite_numbers.keys():
		print("Hi " + name.title() +
			", I see your favorute number is " +
			str(favorite_numbers[name]) + " what a buttlord.")

	else:
		print("Hey " + name.title() + " your a dummy for not answering")

	

	

