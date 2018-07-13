guest_list = ['emily', 'subhan', 'arusa']



print("Unfortunately I am only able to have one person to eat dinner with!\n")

guest_list.insert(0, 'ike')
guest_list.insert(2, 'marth')
guest_list.append('lucina')


guest_list_amount = len(guest_list)

print(str(guest_list_amount))

first_guest_popped = guest_list.pop(1)
second_guest_popped = guest_list.pop(2)
third_guest_popped = guest_list.pop(3)
fourth_guest_popped = guest_list.pop()
fifth_guest_popped = guest_list.pop(-1)





print(guest_list[0]	.title() + " you still get to eat with me! Yay!")

print(first_guest_popped.title() + " I'm sorry but I cannot invite you to dinner!")
print(second_guest_popped.title() + " I'm sorry but I cannot invite you to dinner!")
print(third_guest_popped.title() + " I'm sorry but I cannot invite you to dinner!")
print(fourth_guest_popped.title() + " I'm sorry but I cannot invite you to dinner!")
print(fifth_guest_popped.title() + " I'm sorry but I cannot invite you to dinner!")

