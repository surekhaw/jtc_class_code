print("Challenge 2.1:")
jamal_murray_3pts_made = 46
# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
fred_vanVleet_3pts_made = 43
# TODO: Create variable here for number of 3 pt shots made by James Harden
james_harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots.")
# TODO: Create print statement here for Fred VanVleet
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanVleet_3pts_made} 3 point shots.")
# TODO: Create print statement here for James Harden
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots.")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
jamal_murray_3pts_attempted = 93
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
fred_vanVleet_3pts_attempted = 110
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
james_harden_3pts_attempted = 109

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, player Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_3pts_attempted} 3 point shot attempts.")
print(f"In the 2020 NBA playoffs, player Fred VanVleet made {fred_vanVleet_3pts_made} 3 point shots and {fred_vanVleet_3pts_attempted} 3 point shot attempts.")
print(f"In the 2020 NBA playoffs, player James Harden made {james_harden_3pts_made} 3 point shots and {james_harden_3pts_attempted} 3 point shot attempts.")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
jamal_murray_3pts_percentage = int(jamal_murray_3pts_made / jamal_murray_3pts_attempted *100)
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
fred_vanVleet_3pts_percentage = int(fred_vanVleet_3pts_made / fred_vanVleet_3pts_attempted *100)
# TODO: Calculate and print the 3 point percentage for James Harden
james_harden_3pts_percentage = int(james_harden_3pts_made / james_harden_3pts_attempted *100)


print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
print(f"In the 2020 NBA playoffs, player Jamal Murray made {jamal_murray_3pts_made} 3 point shots. \n\
He made {jamal_murray_3pts_attempted} 3 point shot attempts for a three point percetage of {jamal_murray_3pts_percentage}")
print(f"In the 2020 NBA playoffs, player Fred VanVleet made {fred_vanVleet_3pts_made} 3 point shots \n\
He made {fred_vanVleet_3pts_attempted} 3 point shot attempts for a three point percentage of {james_harden_3pts_percentage}.")
print(f"In the 2020 NBA playoffs, player James Harden made {james_harden_3pts_made} 3 point shots \n\
He made {james_harden_3pts_attempted} 3 point shot attempts for a three point percentage of {james_harden_3pts_percentage}.")


print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print(f"The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \n\
	They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \n\
	Those three have made good developments with the Pelicans, especially Brandon Ingram. \n\
	But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \n\
	Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \n\
	The Lakers ended the season atop the Western Conference with a record of 49-14. \n\
	They were narrowly behind the Bucks for the best record in the league. \n\
	Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \n\
	Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season. ")

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
lakers_are_best = True
# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f"It's {lakers_are_best}! Lakers are the best!")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
print(int(lakers_are_best))
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(float(lakers_are_best))

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
print(str(jamal_murray_3pts_percentage))
print(str(fred_vanVleet_3pts_percentage))
print(str(james_harden_3pts_percentage))

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(int(jamal_murray_3pts_percentage))
print(int(fred_vanVleet_3pts_percentage))
print(int(james_harden_3pts_percentage))


 