from largest_func import largest
from largest_func import minimum
from largest_func import maximum
from largest_func import is_palindrome


def test_largest_function():
	assert largest(1, 2, 3) == 3
	assert largest(10, 15, 30) == 30

def test_minimum_function():
	assert minimum(1, 2, 3) == 1
	assert minimum(10, 2, 15) == 2
	assert minimum(34, 45, 67) == 34
	assert minimum(23, 34, 10) == 10

def test_maximum_function():
	assert maximum(1, 3, 2) == 3
	assert maximum(10, 2, 15) == 15
	assert maximum(23, 34, 10) == 34


def test_palindrome_function():
	assert is_palindrome("tundeednut") == True 
	assert is_palindrome("musa") == False 
	assert is_palindrome("dad") == True 
	assert is_palindrome("12121") == True 
	assert is_palindrome("12345") == False 
	assert is_palindrome("madam") == True 
	assert is_palindrome("is") == False
	assert is_palindrome("o") == True
	

