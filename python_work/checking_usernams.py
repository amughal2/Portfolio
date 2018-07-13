current_users = ['hunk', 'BrOwn', 'flinT', "Yuna", "lyn"]

new_users = ['skyWalkeR', 'dOOku', 'flinT', 'steIn', "BrOwn"]

new_user = [new_user.lower() for new_user in new_users]
current_user = [current_user.lower() for current_user in current_users]

for available_user in new_user:
	if available_user in current_user:
		print("Sorry, the user name " + available_user +  " is not available")
	else:
		print("Hello, the user name ''" + available_user + "'' is available.")

print("\nHave a nice day!")