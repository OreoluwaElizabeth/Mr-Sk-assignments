def length(string):

	return len(string)

def length_two(string):

	if len(string) < 2:
		return ""
	else:
		return string[:2] + string[-2:]

def length_three(string):

	if len(string) < 3:
		return string
	elif string[-3:] == "ing":
		return string + "ly"
	else:
		return string + "ing"

def find_longest_word(words):

	longest_word = ""
	longest_length = 0

	for word in words:
		if len(word) > longest_length:
			longest_word = word
			longest_length = len(word)

	return longest_word, longest_length

def odd_characters(string):
	new_string = ""
	for i in range(len(string)):
		if i % 2 == 1:
			new_string += string[i]
	return new_string

def two_inputs(string, num):

	if type(string) and type(num) in [string, int]:
		return string * num
	else:
		return string 

def minimum(numbers):

	minimum = numbers[0]

	for number in numbers[1:]:
		if number < minimum:  
			minimum = number
	return minimum


def maximum(numbers):

	maximum = numbers[0]

	for number in numbers[1:]:
		if number > maximum:
			maximum = number
	return maximum

def squared(numbers):
	squared_numbers = []
	for number in numbers:

		squared_numbers.append(number * number)

	return squared_numbers

def sum_of_squares(numbers):
	sum_squares = 0
	for number in numbers:

		sum_squares += number * number

	return sum_squares


