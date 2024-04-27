def largest(number1, number2, number3):

	largest = 0

	if number1 > largest and number1 > number2 and number1 > number3:
		largest = number1

	elif number2 > largest and number2 > number1 and number2 > number3:
		largest = number2

	elif number3 > largest and number3 > number2 and number3 > number1:
		largest = number3

	return largest


def minimum(num1, num2, num3):

	minimum = num1

	if num2 < minimum:
		minimum = num2

	elif num3 < minimum:
		minimum = num3

	return minimum

def maximum(num1, num2, num3):

	maximum = num1

	if num2 > maximum:
		maximum = num2

	elif num3 > maximum:
		maximum = num3

	return maximum

def is_palindrome(word):

	reversed_string = "" + word
	for i in range(len(word)-1, -1, -1):
		if word[0] == word[-1]:
			return True 

	else:
		return False