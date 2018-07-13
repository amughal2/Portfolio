players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players of my team:")
for player in players[:3]:
	print(player)
print("The middle three players in my team are:")
for player in players[1:4]:
	print(player)
print("The last three players in my team are:")
for player in players[-3:]:
	print(player)