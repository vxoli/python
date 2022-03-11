# Python Challenge #4
# Return index of all matching items in a list

def index_all(search_list, item):
	indicies = list()
	for i in range(len(search_list)):
		if search_list[i] == item:
			indicies.append([i])
		elif isinstance(search_list[i],list):
			for index in index_all(search_list[i],item):
				indicies.append([i]+index)
	return indicies

example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

print(index_all(example,2))