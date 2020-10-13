# # for
# # for x in y:
# # #	i.e. for each x in the list of y:

# # groceries = ['apples', 'oranges']
# # "for each (fruit) in the list of (groceries":

# numbers = [12, 8, 3]

# for num in numbers: #name of variable not matter - could say for "spaghetti"
# 	print(num) #indentation matters! must indent so it knows you're inside loop
# 	print('hello world')
# print('hi again!')

# times = []

# for num in numbers:
# 	times.append(num * 2)

# print(times)

#complicated operations in lops

# # lower case strings
# lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']

# # upper case strings
# upper_list = []

# for i in lower_list:
# 	upper_list.append(i.upper())

# print(upper_list)

# mixed data types

# mixed = [23, 'word', 23.4, True]
# # upper case strings
# data_types = []

# for data in mixed:
# 	data_types.append(type(data))
# 	print('iteration', data_types)

# 	# # for loop is done, run the rest
# 	# print('independent print', data_types) #note this prints for each i because of indentation

# # for loop is done, run the rest
# print('independent print', data_types) #note this prints for each i because of indentation

# only lists and strings are iterable
# my_string = 'ice cream'

# for char in my_string:
# 	print('iteration', char) #this only works in strings

# long_num = 1000000

# for digit in long_num:
# 	print(digit) #does not work unless string or list

# my_string = "ice cream"
# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in my_string:
# 	if char in vowels:
# 		print(f'{char} is a vowel')
# 	else:
# 		print(f'{char} is not a vowel')


# range() function
# for i in range(100):
# 	print(i)

# lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']

# # range() # takes a number
# # len() #takes a list -> number of items, length of list

# for i in range(len(lower_list)):
# 	lower_list[i] = lower_list[i].capitalize()

# print(lower_list)

# while
count = 0

while count < 5:
	# code block runs infinitely as long as count < 5
	# as long as condition is rue, it will conitnue to run code
	print(count)
	count = count +1

print('done', count)

