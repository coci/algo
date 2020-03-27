# implementation of counting sort

"""
to sort elements that we can categorize them with order of O(N^2)
for example sort n element in 5 category
"""

def counting_sort(array):
    max_value = max(array)
    counting = [0] * (max_value + 1)

    for i in array :
        counting[i] += 1

    soret_array = []

    for i in range(max_value+1)
        soret_array += [i] * counting[i]
    
    return soret_array