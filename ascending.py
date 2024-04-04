number = float(input('Enter number:\n'))

number2 = float(input('Enter number:\n'))

number3 = float(input('Enter number:\n'))

if number < number2 and number < number3 and number2 < number3:
	print(number,  number2,  number3)

if number2 < number and number2 < number3 and number3 < number:
	print(number2,  number3,  number)

if number3 < number and number3 < number2 and number2 < number:
	print(number3,  number2,  number)