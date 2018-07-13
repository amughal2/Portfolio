def build_car (car_name, car_type, **car_detail):

	cars = {}
	cars['car_make'] = car_name
	cars['car_model'] = car_type
	for key, value in car_detail.items():
		cars['key'] = value

	return cars

car = build_car('subaru', 'wrx', engine = 'turbo', color = 'blue')
print(car)