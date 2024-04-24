largest_1 = float('-inf')
largest_2 = float('-inf')

for i in range(10):
	number = float(input("Enter number {i + 1}: "))

	if number > largest_1:
		largest_2 = largest_1
		largest_1 = number

	elif number > largest_2 and number != largest_1:
		largest_2 = number

print(f"The two largest values are: {largest_1} and {largest_2}")

