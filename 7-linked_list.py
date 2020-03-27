# implementation of linked list

"""
>>> one = Node(1)
>>> two = Node("example")
>>> three = Node("5")
>>> four = Node(True)
>>> li = LinkedList()
>>> li.head = one
>>> li.head.next = two
>>> two.next = three
>>> three.next = four
"""
class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.item)
            temp = temp.next


