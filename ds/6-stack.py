# implementaion of stack data structure
"""
stack is a linear data structure that last item inserted will be remove first  .
in stack we can add item in end of list wiht push(item) and remove last item of list with pop() command .
last in - first out => LIFO
"""

class Stack:

    def __init__(self):
        self.array = [] # create empty list

    def push(self,element):
        """ add item at end of list """
        self.array.append(element)  # we use append() to insert item at end of list

    def pop(self):
        """ remove and return last item of list """
        return self.array.pop()
    
    def peek(self):
        """ only return last item of list """
        return self.array[-1]
    
    def is_empty(self):
        """ check is stack got empty """
        return True if len(self.array) < 1 else False
    
    def size(self):
        """ return length of stack """
        return len(self.array)
    