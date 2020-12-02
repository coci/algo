# implementation of selection sort

"""
to sort array
"""

def find_biggest_item(array):
    biggest_item = 0
    for i in array:
        if i > biggest_item:
            biggest_item = i
    return array.index(biggest_item)

def selection_sort(array):
    sorted_array = []
    for _ in range(len(array)):
        biggest_item = find_biggest_item(array)
        sorted_array.append(array.pop(biggest_item))
    return sorted_array[::-1]