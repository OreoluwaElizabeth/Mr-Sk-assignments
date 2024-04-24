while True:

	result = int(input('Enter result (1 or 2): '))

	if result in (1, 2):

		print("Valid")
	else:

		print("Invalid input. Enter 1 or 2.")


passes = 0

failures = 0

for student in range(10):

	result = int(input('Enter result (1 or 2): '))
	passes += 1

failures = 10 - passes

print('Passed:', passes)
print('Failed:', failures)