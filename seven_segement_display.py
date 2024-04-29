print("Welcome to 7-segment display")

for _ in range(10):

	number = int(input("Enter a number to display: "))

	match number:
		case 0:
			print(""" _
| |
|_|""")

		case 1:
			print(""" 
 |
 |""")

		case 2:
			print(""" _
 _|
|_ """)

		case 3:
			print("""_
_|\n_|""")

		case 4:
			print("""|_|\n  |""")

		case 5:
			
			print(""" _
|_ 
 _|""")

		case 6:
			print(""" _
|_ 
|_|""")

		case 7:
			print("""_
 |
 | """)

		case 8:
			print(""" _
|_|\n|_|""")

		case 9:
			print(""" _
|_|\n _|""")

		case _:
			print("Invalid number. Please enter a number between 0 and 9.")

