#alien_0 = {}

#alien_0['color'] = 'green'
#alien_0['points'] = 5

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

#alien_0 = {'color': 'green'}
#print("The alien is " + alien_0['color'] + ".")

#alien_0 = {'color': 'yellow'}
#print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original X position: " + str(alien_0['x_position']))

alien_0['speed'] = 3
#Move Alien to the right
#Determine how far to move the alien based on its speed
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien
	x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

alien_1 = {'color': 'green', 'points': 5}
print("\n")
print(alien_1)

del alien_1['points']
print(alien_1)