name = str(input('Enter your name:\n'))

percentage = int(input('Enter percentage discount:\n'))

counter = 0
total_cost = 0
cost_item = 0

while cost_item != -1: 
	cost_item = int(input('Enter cost for item or -1 to quit:'))

	if cost_item == -1: 
		break

	total_cost += cost_item

	counter += 1

DISCOUNT_FEE = 200
discount_rate = 0.1
discount = total_cost * discount_rate
discounted_amount = total_cost - discount

if total_cost >= DISCOUNT_FEE:
	print(f"Customer name: {name}\nPercentage discount: {percentage}\nOriginal cost: {total_cost}\nDiscounted cost: {discounted_amount:.2f}\nThanks for your patronage!")

else:
	print(f"Customer name: {name}\nPercentage discount: {percentage}\nOriginal cost: {total_cost}\nDiscounted cost: (no discount added)\nThanks for your patronage!")