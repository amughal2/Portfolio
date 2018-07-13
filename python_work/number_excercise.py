numbers = list(range(1,1000001))
minimum = min(numbers)
print(minimum)
maximum = max(numbers)
print(maximum)
the_sum = sum(numbers)
print(the_sum)

odd_numbers = list(range(1,21,2))
for odds in odd_numbers:
	print(odds)

three_multiples = [value**3 for value in range(1,11)]
print(three_multiples)

cube = []
for threes in range(1,11):
	cube.append(threes**3)

print(cube)