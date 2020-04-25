from collections import deque
# all way to check Palindrom


# solution 1
def palindrome_reverse(string):
    return string == string[::-1]


# solution 1
def palindrome_deque(string):
    de = deque()
    for i in string:
        de.append(i)
    state = True
    while len(de) > 1 and state :
        if not de.popleft() == de.pop():
            state = False
    return state


# solution 2
def palindrome_comparison(string):
    array = list(string)
    pivot = (0+len(string)) // 2
    state = True
    index = 0
    while index < pivot and state :
        for k in array:
            if not k == string[len(string) - string.index(k) - 1 ]:
                state = False
            index += 1
    return state