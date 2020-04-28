#!python

from LList.linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        if self.list.length() == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) since we have direct access to TAIL node --> append()"""
        # Insert given item
        self.list.append(item) # add item after Tail node
        # self.list.prepend(item) # add item before Head node

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if not self.is_empty():
            return self.list.head.data # return head node data
            # return self.list.tail.data # return tail node data
        return None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) intant access to head --> .delete(front)"""
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError("Empty Queue!")

        front = self.list.head.data # Define front to be head node
        # front = self.list.tail.data # Define front to be tail node
        self.list.delete(front)
        return front

    def push_front(self, item):
        """Insert item to the front of the queue.
        Running time: O(1) since we have directt access to the HEAD node."""
        self.list.append(item)

    def push_back(self, item):
        """Insert item to the back of the queue.
        Running time: O(1) since we have direct access to the TAIL node."""
        self.list.prepend(item)

    def pop_front(self):
        """Delete item at the front of the queue. Raise ValueError if the
        queue is empty.
        Running time: O(1) since we have direct access to the HEAD node.
        """
        if self.is_empty():
            raise ValueError("Queue is Empty")

        front = self.list.head.data
        self.list.delete(front)

        return front

    def pop_back(self):
        """Delete item at the back of the queue. Raise ValueError if the
        queue is empty.
        Running time: O(n) since we have to iterate the length of the linked list.
        """
        if self.is_empty():
            raise ValueError("Queue is Empty")

        back = self.list.tail.data
        self.list.delete(back)

        return back


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        if not self.list:
            return True
        else:
            return False


    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list) # length of list


    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) directly adds to back node"""
        # Insert given item
        self.list.append(item) # insert item to the last index in list
        # self.list.insert(0, item) # insert item to the first index in list

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if not self.list:
            return None
        else:
            return self.list[0] # return index 0
            # return self.list[self.length() - 1] # return index n - 1

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) directly removes item from front"""
        # Remove and return front item, if any
        if len(self.list) > 0:
            return self.list.pop(0) # remove item in index 0 and return it
            # return self.list.pop(self.length() - 1) # remove item in index n - 1 and return it
        else:
            raise ValueError


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# Queue = ArrayQueue # SOME OF THESE TESTS WILL FAIL BECAUSE OF THE LINKED LIST STRETCH CHALLENGES I IMPLEMENTED
