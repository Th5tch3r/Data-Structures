"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.

3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   Answer: I think the difference is that for linked list, we cannot just take out any item 
   like the array. For array it is possible to just grab out an item using their array's order
   or key. However for linked list we have to be careful to not just dequeue because everything 
   in is arranged based on their order of connection, 1 missing item can cause an error.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# Queue with an array
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.storage != []:
            return self.storage.pop(0)
        else:
            return None

# Queue with a linked list
from singly_linked_list import LinkedList

class QueueLinked:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size
    
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()
