def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

my_profile = build_profile('adil', 'mughal', occupation= 'student', field= 'computer information systems')
print("hello")
print(my_profile)