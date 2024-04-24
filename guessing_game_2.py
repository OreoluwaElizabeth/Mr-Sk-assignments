import random

number = random.randrange(1, 10)

guess_number = 0

while guess_number != number:

	guess_number = int(input("Enter a lucky number between 1-10: "))

	if guess_number == number:

		print("Yay you won!!! Good job :)")

		break

	elif guess_number < 1 or guess_number > 10:

		print("Enter correct number keep trying :)")

	elif guess_number != number:

		print("You failed!!! Try again next time :)")

