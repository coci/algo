#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,item):
        self.data = item
    def setNext(self,item):
        self.next = item


class UnorderdList:

    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.getNext()
        return count
    def search(self,item):
        current = self.head
        found = False
        while current and not found:
            if current.getData() == item :
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        pervious = None
        found = False

        while not found:
            if current.getData() == item :
                found = True
            else :
                 pervious = current
                 current = current.getNext()

        if pervious == None :
            self.head = current.getNext()
        else:
            pervious.setNext(current.getNext())
    # add append(i)
    # add insert(p,i)
    # add index(i)
    # add pop()
    # add pop(p)



class OrderedList:

    def __init__(self):
        self.head = None
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self,item):
        current = self.head
        pervious = None
        stop = False
        while current and not stop:
            if current.getData() > item :
                stop = True
            else:
                pervious = current
                current = current.getNext()
        temp = Node(item)
        if pervious == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            pervious.setNext(temp)
    
