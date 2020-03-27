# implementation of Queue

"""
>>> q = Queue()
>>> q.enqueue(1)
>>> q.enqueue(2)
>>> q.enqueue(3)
>>> q.dequeue()
>>> 1
"""
class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self,element):
        self.array.insert(0,element)
    
    def dequeue(self):
        return self.array.pop()
    
    def is_empty(self):
        return True if len(self.array) < 1 else False
    
    def size(self):
        return len(self.array)