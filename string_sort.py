# Python Challenge 3 from LinkedIn Learning
# Sort the words in a string alphabetically

def sort_list(list):
	list = list.split(' ')
	list.sort(key=lambda x:(x.lower(), x))
	return list

words = 'Hello this is the first string'
print(words)
sorted = sort_list(words)
print(sorted)