# implementation of Deque

"""
assum this is a Deque :
                                    this is Deque
                        ------------------------------------------  
this is Read ==>        task 1| task 2 | task 3 | task 4 | task 5     < === this is Front
                        ------------------------------------------


command                   |          result
-------------------------------------------------
    d = Deque()           |       []
-------------------------------------------------
    d.addRear(4)          |      [4]
-------------------------------------------------
    d.addFront("dog")     |    [4,"dog"]
-------------------------------------------------
    d.addRear("7")        |    ["7" , 4 , "dog"]
-------------------------------------------------
    d.addFront(True)      | ["7" , 4 , "dog",True]
-------------------------------------------------
    d.removeRear()        |  [4 , "dog",True]



"""
class Deque:
    
    def __init__(self):
        self.array = []

    def addFront(self,item):
        self.array.append(item)

    def addRear(self,item):
        self.array.insert(0,item)
    
    def removeFront(self):
        return self.array.pop()

    def removeRear(self):
        return self.array.pop(0)
    
    def isEmpty(self):
        return True if len(self.array) < 1 else False
    
    def size(self):
        return len(self.array)