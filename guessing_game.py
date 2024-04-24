WINNING_NUMBER = 8

for i in range (1, 4):

	guess_number = int(input("Enter a lucky number between 1-10: "))


	if guess_number == WINNING_NUMBER:
		
		print("You Won !!!")

		break

	else :
		print("You loosed, Try again later !!!")