# implementation of binary search

"""
to sort array with recursion
"""

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[(0+len(array)-1) // 2]
        array.pop((0+len(array)-1) // 2)
        less_items = [x for x in array if x <= pivot]
        greather_items = [x for x in array if x > pivot]
        return quick_sort(less_items) + [pivot] + quick_sort(greather_items)
        