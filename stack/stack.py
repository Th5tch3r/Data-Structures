"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.

3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   Answer: I think for stack, it would be easier to work with a linked list since whatever
   comes in last, have to leave first. As for linked list, it is better this way
   because it doesn't need to care about the connection between the items in this list.
   And for array, I think it is going to be not a big problem because it does not depend
   on the order.

"""
# Stack using an array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.insert(0, value)

    def pop(self):
        if self.storage != []:
            return self.storage.pop(0)
        else:
            return None

# Stack using a Linked List
from singly_linked_list import LinkedList

class StackLinked:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()