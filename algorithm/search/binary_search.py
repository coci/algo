# implementation of binary search
"""
to search an element in soretd list we use binary search with order of  O(LogN)

>>> array = [1,2,3,4,5,6]
>>> binary_search(array,2)
>>> 1  # 1 is index of item 2 in array
"""


def binary_search(array , element):
    """
    binary search

    parameters :
        - name : array
            - type : list
            - description : soretd list of itme

        - name : element
            - description : an element we look for
    responses :
        None if element doesn't in list else index of item
    """
    low_bound = 0
    high_bound = len(array) - 1

    while low_bound < high_bound:
        middle_index = (low_bound + high_bound) // 2
        guess_item = array[middle_index]

        if guess_item == element:
            return middle_index
        elif guess_item > element :
            high_bound = middle_index - 1
        else:
            low_bound = middle_index + 1
    return None


# improve binary search

def binary_search(array, element):
    pass