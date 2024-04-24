PRINCIPAL = 1000

RATE = 0.07

for year in range(1, 31):

	amount = PRINCIPAL * (1 + RATE) ** year

	print(f"Year {year}  {amount:.2f}")
