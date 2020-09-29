# escape line \  - this makes reading code easier not having a long string on one line
lyrics = "At first I was afraid, I was petrified.  Kept thinking how I \
cold never live without you by my side."

# newline \n
lyrics = "At first I was afraid, I was petrified.\n Kept thinking how I \
cold never live without you by my side."

# tab character \t
lyrics = "At first I was afraid, I was petrified.\n\t  Kept thinking how I \
cold never live without you by my side."

#formatted string / f-string
profit = 120
my_f_string = f"The profit today is {profit+1000}"

# putting 2 strings together
fruit1 = "apple"
fruit2 = "banana"
fruit3 = fruit1 + fruit2
print(fruit3)
print(fruit1 + ' ' + fruit2 + ' ' + 'orange')

# make uppercase / lowercase
print(fruit3.upper())
print(fruit3.lower())

# strings can have numbers
my_string2 = '2'
print(type(my_string2))

# boolean variables - true / false
i = True
j = int(i)
print(j) # prints 1 because false = 0 and true = 1s
