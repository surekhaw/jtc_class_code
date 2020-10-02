# dictionaries

blank_dict = {}
print(type(blank_dict))

# variable
username = 'Ash'

# list
user_account_as_list = ['pbloom', 270.26]

# dictionary
user_account = {
	'username': 'pbloom',
	'balance': 270.26
}

print(user_account['username'])

# adding a new key:value
user_account['last_transaction_date'] = '9/15/2020'

print(user_account)
print(user_account['last_transaction_date'])

user_account['user_birthyear'] = 1993

print(user_account['user_birthyear'])

# update key:value pair
user_account['balance'] = 500.00
print(user_account['balance'])

#remove key:value pair
user_account.pop('user_birthyear')
print(user_account)

groceries_dict = {
	'fruits': ['apples', 'bananas', 'oranges'],
	'vegetables': ['carrots', 'zucchini']
}

print(groceries_dict['fruits'])

# dictionary inside dictionary
blank_dict = {}
groceries_dict = {
	'fruits': blank_dict,
	'vegetables': ['carrots', 'zucchini']
	'random': 23432
}

# list vs. dictionary: okay just look up index in list, but must know key to look up in dictionary
