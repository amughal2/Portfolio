number_list = [1,2,3,4,5,6,7,8,9]

for string_number in number_list:
	if string_number >= 4:
		print(str(string_number) + "th")
	elif string_number == 3:
		print(str(string_number) + "rd")
	else:
		print(str(string_number) + "nd")