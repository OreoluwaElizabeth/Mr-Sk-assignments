grade = int(input('Enter a score:\n'))

if grade > 80 and grade <= 100 :
	print(f'Your score is {grade} and your grade is A')
elif grade > 65 and grade <= 79 :
	print(f'Your score is {grade} and your grade is B')
elif grade > 50 and grade <= 64 :
	print(f'Your score is {grade} and your grade is C')
elif grade > 40 and grade <= 49 :
	print(f'Your score is {grade} and your grade is D')
elif grade > 100:
	print('Invalid score')
else:
	print('invalid score')
	
