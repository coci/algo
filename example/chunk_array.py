"""
chunk([1,2,3,4],2) => [[1,2],[3,4]]
chunk([1,2,3,4,5],2) => [[1,2],[3,4],[5]]
chunk([1,2,3,4,5],10) => [[1,2,3,4,5]]
"""

def chunk_with_recursion(array,part):
    """
    we can split array into sub array with recursion :
        all we need is split given array into given part :
        array = [1,2,3,4]
        part = 2
        final result => [[1,2],[3,4]]

        to that all we need is split array into sub array , so we can use slice method in python
        >>> array = [1,2,3,4]
        >>> array[:2]
        [1,2]

        now we need divide our array into subarray with recursion.
    """
    if len(array) <= part :
        return [array]
    else:
        return [array[:part]] + chunk_with_recursion(array[part:],part)



def chunk_without_recursion(array,part):
    result = []

    while len(array) > part :
        result.append(array[:part])
        array = array[part:]
    result.append(array)
    return result