# implementation of insertion sort
"""
to sort array with order of O(n^2)
"""

def insertion_sort(array):
    
    for k in range(len(array)):
        index = k
        item = array[k]
        while index > 0 and array[index - 1] > item :
            array[index] = array[index-1]
            index -= 1
        array[index] = item
    return array  