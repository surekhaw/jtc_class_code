# make a grocery list
# lists have particular order
groceries = ['eggs', 'meat', 'pasta']
print(groceries)
print(type(groceries))

groceries = ['eggs', 'meat' 'pasta']
print(groceries)

# add items to end of list with .append
groceries.append(4.0)
groceries.append('kumquat')
groceries.append('potato')
groceries.append(True)
print(groceries)

# remove items with .remove
# must specify what you want removed
groceries.remove('kumquat')
groceries.remove(4.0)
groceries.remove(True)

# use .len() to get length of list
print(len(groceries))

# list indexing 
# zero based
print(groceries[0])

# negative list indexing
# -1 gives last item on list
print(groceries[-1])

#slicing
# indexing multiple items, but not the last one
new_list = groceries[0:2] #gives 0 and 1, but not 2 - up to but not including
print(new_list)

#splitting and joining - list must be strings
grocery_string = ' '.join(groceries) #join items with a space in between into one combined string
print(grocery_string)

grocery_string = 'FOOD'.join(groceries)
print(grocery_string)

my_string = 'carrots, rice, peas, avocados'
my_list = my_string.split('o') # split by 'o's
print(my_list)