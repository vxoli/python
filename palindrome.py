# Python Challenge 2 from LinkedIn Learning
# Detect Palindrome
import re

def is_palindrome(txt):
	return "".join(re.findall(r'[a-z]+', txt.lower())) == "".join(re.findall(r'[a-z]+', txt.lower()))[::-1] 
	# Returns True for Palindrome or False if not
	# ignores whitespace and non-alphabet characters. evaluates in lowercase

print(is_palindrome("Hello world"))
print(is_palindrome("Go hang a salami - I'm a lasagna hog"))