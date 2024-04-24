number = int(input("Enter a five-digit integer: "))

if number < 10000 or number >= 100000:
	print("Invalid input")

else:
	original_number = number
	reversed_integer = 0

	while number > 0:
		digit = number % 10
		reversed_integer = reversed_integer * 10 + digit
		number //= 10

	if original_number == reversed_integer:
		print(f"{original_number} is a palindrome.")
	else:
		print(f"{original_number} is not a palindrome.")