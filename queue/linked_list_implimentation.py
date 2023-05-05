# linked list implementation of queue data structure

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        

class Queue:
    
    def __init__(self):
        self.front = self.rear = None
        
    def isEmpty(self):
        ''' return if queue is empty'''
        return self.front == None
        # return self.rear == None #possible alternative
        
    def Enqueue(self, item):
        temp = Node(item)
        
        # if  queue have only one element
        if self.rear == None:
            self.rear = self.front = temp
            return
        
        
    
    


