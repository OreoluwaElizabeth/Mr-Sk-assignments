sum = 0

for num in range(1, 20001):

    if num % 10 == 0:
        sum += num

print("The sum of multiples of 10 between 1 and 20,000 is : ", sum)