# # loops review
# my_strings = ['watermelon', 'new york', 'houston', 'stockholm', ]

# #make loop to iterate through my_strings and print them out one at a time
# for element in my_strings:
# 	print(element)

# # printig whole list each time
# for element in my_strings:
# 	print(element)

# # use rnage()
# for i in range(10):
# 	print(i)
# a = 'hello'
# b = 'goodbye'
# for i in range(11):
# 	print(a)
# 	print(b)
# print(b)

# nested loops
days = ['monday', 'tueday', 'wednesday', 'thurs', 'friday', 'sat', 'sun']

# outer loop loops through days
for day in days:
	print(day)
	# for each day, print each letter individually
	# inner loop - note additional indentation
	for letter in day:
			print(letter)

# not nested
for day in days:
		print(day)
		print(day[1])
		print(letter.upper())

# nested with range  - inner loop occurs faster because it keeps going while outer var is constant
for outer_var in range(3):
	for inner_var in range(3):
		print(f'outer: {outer_var}, inner: {inner_var}')
print(inner_var) # not an error!  after loop, if not change variable, keeps value at end fo loop


# loops with logic statements
for day in days: 
	if day.startswith('s'):
		print(f'{day} is a weekend') #without indent, get error because then nothing is inside erro
	#e.g. if print statements started back here
	else:
		print(f'{day} is a weekday')
		if 'o' in day:
			print('contains o')

# break - break out of loop
for day in days:
	print(day)
	if day.startswith('f'):
		break
print('done with loop')