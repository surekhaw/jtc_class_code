# # Logical operators
# # Using symbols to compare values
# # - and, or, not - combine logical statements
# # conditionals, if and else 

# # math comparisons
# print(1>0)

# a=0
# b=1
# c=1

# print(f"is a equal to b?: {a==b}")
# print(f"is a not equal to b?: {a!=b}")
# print(f"is a greater than b?: {a > b}")
# print(f"is a less than b?: {a < b}")
# print(f"is b greater than or equal to c?: {b >= c}")
# print(f"is b less than or equal to c?: {b <= c}")

# # integers vs. floats
# print(3 == 3.000)

# # booleans
# print(True == 1)

# a = 'cat'
# b = "cat"
# c = "Cat"

# print(a==b)
# print(a != c)
# print('cat' > 'dog')

# compounding logic (or, an & not)

# or
# print(2 < 3 or 4 < 3)
# print(2 > 3 or 4 > 3)
# print(2 > 3 or 4 < 3)
# print(2 < 3 or 4 > 3)

# and
# print(2 < 3 and 4 < 3)
# print(2 > 3 and 4 > 3)
# print(2 > 3 and 4 < 3)
# print(2 < 3 and 4 > 3)

# not - flips statement.  If it would give true, flip it to false and vice versa
# print(not 2 > 3)
# print(not False)
# print(not True)

# a = 1
# b = 2
# print(a < 10 and not a > b)

# conditionals
# a = 5
# # if a > 3:
# # 	# if condition is true, run code below
# # 	print('greater than 3!')
# # 	print('hello this was an if statement')

# if a == 3:
# 	# if condition is not true, won't run code below
# 	print('greater than 3!')
# 	print('hello this was an if statement')
# else:
# 	# it will run code below instead
# 	print('not equal 3!')
# 	print(f'{a} not equal 3!')

# a = 2
# if a < 0:
# 	print('a is a negative number')
# elif a > 0:
# 	print('a is a positive number')
# else:  # not required to have an else
# 	print('this is probably never run')

# season = 'fall'
# if season == 'spring':
# 	print('getting warmer')
# elif season == 'winter':
# 	print('cold out')
# elif season == 'summer':
# 	print('hot out')
# else:
# 	print('getting colder')

# multiple ifs will work, but better to use elif
# a = 2
# b = 30

# if a > 10:
# 	print('a greater than 10')
# if b > 10:
# 	print('b greater than 10')

# a = 10

# if a > 0:
# 	print('a is positive')
# 	# nest if statement
# 	if a > 10:
# 		print('a is greater than 10')
# 	else:
# 		print("a is not greater than 10")
