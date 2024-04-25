from snack_func import length
from snack_func import length_two
from snack_func import length_three
from snack_func import find_longest_word
from snack_func import odd_characters
from snack_func import two_inputs
from snack_func import minimum

def test_length_function():
	assert length("semicolon") == 9
	assert length("oreoluwa") == 8
	assert length("skiru") == 5

def test_length_two_function():
	assert length_two('semicolon') == 'seon'
	assert length_two('on') == 'onon'
	assert length_two('o') == ""

def test_length_three_function():
	assert length_three('abc') == 'abcing'
	assert length_three('string') == 'stringly'
	assert length_three('on') == 'on'

def test_longest_word_function():

	words = ["welcome", "out", "weather", "mobile", "breakfast", "journey"]
	longest_word, longest_length = find_longest_word(words)

	assert longest_word == "breakfast" and longest_length == 9

def test_odd_characters_function():
	assert odd_characters('semicolon') == 'eioo'

def test_two_inputs_function():
	assert two_inputs('hello', 3) == 'hellohellohello'
	assert two_inputs('hi', 4.5) == 'hi'

def test_minimum_function():

	numbers = [8, 4, 9, 2, 5, 7, 3] 
	assert minimum == 2
 
	
