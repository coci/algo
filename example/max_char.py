"""
 --- Directions
Given a string, return the character that is most
commonly used in the string.
--- Examples
max_char("abcccccccd") === "c"
max_char("apple 1231111") === "1"



**Tips and trick ** : 
    
    you can apply this technique for :
        - what is the most common character in given string ?
        - Does string a have the same characters as string b ( is it anagram ) ?
        - Dose the given string have repeated characters in ?
"""
from collections import Counter

def max_character(string):
    """
    steps :

    to find maximum character we can count each indivitual character and find what is the most repeated :

    exmample :

    string => "hello world"
    
    count_chracter => 
                        { 
                            "h" : 1,
                            "e" : 3,
                            "l" : 3,
                            "o" : 2,
                            "" : 1,
                            "d" : 1
                        }   

    now we can walk through dictionary and find most repeated character ,
    there is a 2 ways to count character in string or any iterable objects :
    
    1 :
        string = "hello world"
        chars = {}
        for i in string:
            if not chars.get(i):
                chars[i] = 1
            else:
                chars[i] + 1

    2 :
        from collections import Counter

        string = "hello world"
        chars = Counter(string)

    **Note** : in this example we use Counter() method .


    to find max_char in dicationary of counting number we have 2 way :
    1 :
        return max(chars, key=lambda k: chars[k])

    2:
        max_val = 0
        max_char = ""

        for k,v in char :
            if v > max_val :
                max_val = v
                max_char = k

        return max_char

    """
    
    chars = Counter(string)

    return max(chars, key=lambda k: chars[k])

    





