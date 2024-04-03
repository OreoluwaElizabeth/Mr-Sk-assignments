number = int(input('Enter a five digit integer:\n'))

first_digit = number // 10000

second_digit = (number / 1000) % 10

third_digit = (number / 100) % 10

fourth_digit = (number / 10) % 10

fifth_digit = number % 10

print(int(first_digit) , int(second_digit) , int(third_digit) , int(fourth_digit) , int(fifth_digit))