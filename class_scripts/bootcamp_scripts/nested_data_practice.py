# # lists inside lists

shopping_list = [['mangos', 'apples', 'oranges'], ['carrots', 'broccoli', 'lettuce'], ['corn flakes', 'oatmeal', 'cheerios']]

# print(shopping_list)

# # access inner list
# print(shopping_list[1])

# # One more level down
# # Access item inside inner list
# print(shopping_list[1][0])

# # Add to inner list
# shopping_list[1].append('avocados')
# shopping_list[1].append('peach')
# shopping_list[1].append('kiwi')

# print(shopping_list)

# nested loops with nested lists
# for food_group in shopping_list:
# 	print(food_group)

# for food_group in shopping_list:
# 	for food in food_group:
# 		print(food)

# # dictionaries inside lists
# users = [{'username': 'ash', 'password': 'ilovepython'}, {'username': 'paul', 'password': 'ilovegit'}, {'username': 'aryn', 'password': 'ilovedictionaries', 'last_login': '9/28/2020'}]
# print(users)

# # print dictionary inside list
# print(users[2])

# # print out an item in a dictionary, in a list
# print(users[2]['last_login'])

# # loop through a list of dictionaries, and get the same infro from each one
# for user in users:
# 	print(user['username'])

# list inside dictionaries
# cart = {'fruit': ['mangos', 'apples'],
# 		'veggies': ['spinach', 'peas'],
# 		'grains': 'rice',
# 		}
# # print(cart)

# # # access a specific list inside a dictionary
# # print(cart['veggies'])

# # # add items to list inside dictionary
# # # because of list, can use append function
# # cart['veggies'].append('peach')
# # cart['veggies'].append('carrots')
# # cart['veggies'].remove('peach')
# # print(cart['veggies'])

# # bracket indexing on a list inside a dictionary
# print(cart['fruit'][0])

# # loop through list inside dictionary
# for food in cart['fruit']:
# 	print(food.upper())

# dictionaries inside dictionaries
restaurants = {'El Basuerero': {'address': '32-17 Steinway Street', 'menu_url': 'menu.com'},
	'Joes Pizza': {'address': '7 Carmine Street', 'phone_number': '718-882-9012'}
}
# print(restaurants)

# # specfic restaurants - search by key
# print(restaurants['Joes Pizza'])

# # specific items inside nested dictionaries
# print(restaurants['Joes Pizza']['phone_number'])

# add new items to dictionary inside dictionary
restaurants['Joes Pizza']['phone_number'] = '718-908-0012'
print(restaurants['Joes Pizza']['phone_number'])