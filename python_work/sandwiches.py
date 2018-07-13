def build_sandwhich (*builds):

	print("\nMaking a sandwhich with: ")
	for build in builds:
		print("- " + build)

build_sandwhich('tuna', 'provolone', 'lettuce', 'onions')