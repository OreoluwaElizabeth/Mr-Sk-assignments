positive_count = 0
negative_count = 0
zero_count = 0

while True:
  user_input = input("Enter a number (or 'done' to finish): ")

  if user_input.lower() == 'done':
    break

  try:
    num = int(user_input)
    if num > 0:
      positive_count += 1
    elif num < 0:
      negative_count += 1
    else:
      zero_count += 1
  except ValueError:
    print("Invalid input.Please enter a number or 'done' . ")

print("Positive numbers entered:" , positive_count)
print("Negative numbers entered:" , negative_count)
print("Zero numbers entered:" , zero_count)









