"""This code determine the weather condition"""

temperature = float(input("Enter the temperature:\n"))

if temperature >= 70:
	print("the weather extremely hot")
elif temperature > 40 and temperature < 70:
	print("the weather is hot")
elif temperature > 20 and temperature <= 40:
	print("the weather is average")
elif temperature >= 1 and temperature <= 20:
	print("the weather is cold")
	print("don't dare to come out or you will die")
	print("better come out with your sweater")
else:
	print("the weather is extremely cold, stay home")

#print(help(input))