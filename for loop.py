from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
#answer(aRandomNumber) is random
# For Testing: print(aRandomNumber)
for i in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
		continue
	else:
		guess = int(guess)
	i += 1 #here so the conditional(turns) applies; if below options, turns=unlimited
	if (guess == aRandomNumber):
		print("Congrats")
		break
	elif (guess > aRandomNumber):
		print("Lower")
		continue
	else:
		print("Higher")
		continue

print("Too bad, GAME OVER")
