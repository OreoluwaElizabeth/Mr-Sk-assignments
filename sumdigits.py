number = int(input("Enter an integer between 0 and 1000: "))

if number < 0 or number > 1000:
    print("Enter a valid integer between 0 and 1000: ")
else:
    sum_of_digits = 0
    remaining_number = number

    while remaining_number != 0:
        sum_of_digits += remaining_number % 10
        remaining_number //= 10

    print("The sum of all digits in the integer", number, "is", sum_of_digits)