import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList as dll  # noqa
from doubly_linked_list import ListNode  # noqa


class Queue:
    def __init__(self):
        self.size = 0
        self.list = dll()

    def enqueue(self, value):
        self.list.add_to_head(value)
        self.size = self.list.length

    def dequeue(self):
        if self.size == 0:
            return(None)
        else:
            val = self.list.remove_from_tail()
            self.size = self.list.length
            return(val)

    def len(self):
        return(self.size)
