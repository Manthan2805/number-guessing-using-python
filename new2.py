import random
print("The numbers are from 1 to 100")
lower = 1
upper = 100

x = random.randint(lower, upper)
print("\n\tYou've only 20 chances to guess the integer!\n")

count = 0

while count < 20 :
	count += 1

	guess = int(input("Guess a number:- "))

	if x == guess:
		print("Congratulations you did it in ",count, " try")
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

if count >7 :
	print("\nThe number is %d" % x)
else:
	print("\tBetter Luck Next time!")
	print("\nRetry the game!!!!!")

