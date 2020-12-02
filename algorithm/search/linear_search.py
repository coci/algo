
"""
implementation of linear search


to search an element in list order of O(n)

>>> array = [1,2,3,4,5,6]
>>> linear_search(array,2)
>>> 1  # 1 is index of item 2 in array
"""

def linear_search(array,element):
	for i in range(len(array)):
		if array[i] == element:
			return i
	return -1

"""
but we can improve our search like this:
linear_search with order of O(n/2)

in this case with each loop we look at the front and back of the array
so we look 2 elements in one step so the algortithm takes O(n/2)

"""
def linear_search(array, element):
	right_bound = 0
	left_bound = len(array) - 1

	while right_bound <= left_bound :
		if array[right_bound] == element:
			return right_bound

		if array[left_bound] == element:
			return left_bound

	return -1