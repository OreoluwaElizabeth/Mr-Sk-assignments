miles = 0

gallons = 0

while True:

	gallons_used = float(input("Enter gallons used (or -1 to quit): "))

	if gallons_used == -1:
		break

	miles_driven = float(input("Enter miles driven: "))

	MPG = miles_driven / gallons_used

	print(f" The miles/gallon for this tank was {MPG:.2f}")

	miles += miles_driven
	gallons += gallons_used

if gallons > 0:
	total_MPG = miles / gallons
	print(f"\n The overall average miles/gallon was {total_MPG:.2f}")
else:
	print("\n No data entered")



