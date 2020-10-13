# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

print('Question 1')
employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name'
lower_name = employee_name.lower()

# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list'
names_list = lower_name.split(' ')

# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names'
joined_names = (".").join(names_list)

# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email'
email =joined_names + "@ripplemedia.com"

print(email)


print('Question 2')

# Congratulations! Your team is expanding. Below is a list of their names:
names = ['Max Bartlett', 'Angelita Norris', 'Stewart Mueller', 'Dominique Henry', 'Carmela Gross', 'Bettie Mcmillan', 'Sara Ellison', 'Ira Anthony', 'Pauline Riley', 'Ben Weber',
         'Joanne Mcknight', 'Loren Gould', 'Jamar Singh', 'Amanda Vance', 'Tyrell Andrade', 'Jana Clements', 'Eddy Mcbride', 'Marsha Meyer', 'Elbert Shannon', 'Alyce Hull']

emails = []

# We want to convert all their names into the same format from Question 1
# 2.1 TODO: Use a "for" loop to go over each name in the names list
for team_member in names:

# 2.2 TODO: Inside the "for" loop, create the email id by re-using the logic from Question 1 and...
	lower_name = team_member.lower()
	names_list = lower_name.split(' ')
	joined_names = (".").join(names_list)
	email = joined_names + "@ripplemedia.com"
	
# 2.3 TODO: ..add the email to the emails list
	emails.append(email)

print(emails)