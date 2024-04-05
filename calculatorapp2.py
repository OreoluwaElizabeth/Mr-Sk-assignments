name = str(input('Enter your name:\n'))

percentage = int(input('Enter percentage discount:\n'))

item_purchased = int(input('Enter number of items purchased:\n'))

counter = 0
total_amount = 0

while counter < item_purchased:
	amount = int(input('Enter items amount:\n'))

	total_amount += amount

	counter += 1

DISCOUNT_FEE = 200
discount_rate = 0.1
discount = total_amount * discount_rate
discounted_amount = total_amount - discount

if total_amount >= DISCOUNT_FEE:
	print(f"Customer name: {name}\nPercentage discount: {percentage}\nOriginal cost: {total_amount}\nDiscounted cost: {discounted_amount:.2f}\nThanks for your patronage!")

else:
	print(f"Customer name: {name}\nPercentage discount: {percentage}\nOriginal cost: {total_amount}\nDiscounted cost: (no discount added)\nThanks for your patronage!")