from collections import deque


#solutuion 1
def reverse_string_indice(string):
    return string[::-1]


#solution 2
def reverse_string_linear(string):
    return "".join([string[len(string)-i-1] for i, _ in enumerate(string)])


#solution 3
def reverse_string_iterator(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string


#solution 4
def reverse_string_stack(string):
    de = deque()
    for i in string:
        de.append(i)
    reversed_string = ""
    while len(de) > 0 :
        reversed_string += de.pop()
    return reversed_string


#solution 5
def reverse_string_recursion(string):
    if len(string) == 1 :
        return string
    else:
        return reverse_string_recursion(string[1:]) + string[0]