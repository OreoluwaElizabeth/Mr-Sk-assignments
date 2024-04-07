largest = float('-inf')
smallest = float('inf')
first_iteration = True

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
       num = float(user_input)

       if first_iteration:
            largest = num
            smallest = num
            first_iteration = False
       else:
            if num > largest:
                largest = num
            if num < smallest:
                smallest = num
    except ValueError:
        print("Please enter a number or 'done' to finish")

if not first_iteration:
    print("Largest number entered:", largest)
    print("Smallest number entered:", smallest)
else:
    print("No numbers were entered.")