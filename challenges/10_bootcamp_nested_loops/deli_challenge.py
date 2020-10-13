
# print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()
meats_cap = []
cheeses_cap = []

for item in meats:
	meats_cap.append(item.capitalize())
	
for item in cheeses:
	cheeses_cap.append(item.capitalize())

# print(meats_cap)
# print(cheeses_cap)

# print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []

for meat in meats_cap:
	for cheese in cheeses_cap:
		sandwiches.append(f'{meat} and {cheese}')

# print(sandwiches)

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
customer_choice = input(f'What kind of sandwich would you like?')

# TODO: Loop over the sandwiches list.
for item in sandwiches:

# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'
	if item == customer_choice:
		print(f'Great choice! 1 {customer_choice} coming right up!')