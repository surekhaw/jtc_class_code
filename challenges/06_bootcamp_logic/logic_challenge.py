print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

a = 1
b = 0
c = (a > b)

print("The value of c is True since a is greater than b.")

print()

print("Code Snippet 2:")

d = (5 > 7) 

print("The value of d is False since 5 is not greater than 7.")

print()


print("Code Snippet 3:")

m = "goat"
n = "goat"

o = (m == n)

print ("The value of o is True.")

print()

print("Code Snippet 4:")

u = 5
v = 2

if u * v == 10:
    print("The product of a and b is 10")
else:
    print("The product of a and b is not 10")

print()

print("Code Snippet 5:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

elif z > x and z < y:
    print("z is between x and y")

else:
    print("z is greater than y")


print()
print()
print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")
# Create variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

Amazon = 3000
Apple = 100
Facebook = 250
Google = 1400
Microsoft = 200
print()


print("Challenge 3.2.2: Taking user input")
name = input('What is your name?')# TODO: Write code to ask the client his name and save it to a variable.
savings = int(input('How much savings do you have?'))# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, \
	'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.3: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

if stock == "amzn":
	stock = "Amazon"
	number_shares = int(savings / Amazon)
elif stock == "aapl":
	stock = "Apple"
	number_shares = int(savings / Apple)
elif stock == 'fb':
	stock = "Facebook"
	number_shares = int(savings / Facebook)
elif stock == 'goog':
	stock = "Google"
	number_shares = int(savings / Google)
else:
	stock = "Microsoft"
	number_shares = int(savings / Microsoft)

print()

print("Challenge 3.2.4: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
# name = Alex
# savings = 5000
# stock = Apple
# number_shares = int(savings / Apple)
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
print(f"{name} has ${savings} in savings and he can buy {number_shares}\
 shares of {stock} at the current price of $100.")


