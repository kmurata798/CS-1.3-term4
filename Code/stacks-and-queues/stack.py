#!python

from LList.linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if self.list.length() == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        #  Count number of items
        # self.list.length()
        return self.list.length() # 0(1) runtime

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) if top is HEAD node, direct access to the top item.
                        O(n) if top is TAIL node, direct access to the top item, but must then reassign the tail node done by traversing through each node until the end."""
        # Push given item
        # self.list.append(item)
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        #  : Return top item, if any
        if not self.is_empty():
            # return self.list.tail.data
            return self.list.head.data
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) if top is HEAD node, directly remove top item
                        O(n) if top is TAIL node, directly remove top item, but then have to reassign the TAIL node to the new 
                        end node, traversing through LL.
        """
        #  : Remove and return top item, if any
        if self.is_empty():
            raise ValueError("Empty Queue!")

        # top = self.list.tail.data
        top = self.list.head.data
        self.list.delete(top)
        return top


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if not self.list:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)


    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) if top is the last index in list, direct access to first index.
                        O(n) if top is the first index in list, direct acces to first index, but have to shift all items over to
                        make space for more items.
        """
        # Insert given item
        self.list.append(item) # add item to end of list
        # self.list.insert(0, item) # add item to beginning of list

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if not self.list:
            return None
        else:
            return self.list[self.length() - 1] # look at last item of list
            # return self.list[0] # look at first item in list

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) if top is last index in list, directly remove top item.
                        O(n) if top is first index in list, directly remove index 0, but then have to shift all items in list over.
        """
        # Remove and return top item, if any
        if len(self.list) > 0:
            temp = self.list[self.length() - 1]
            self.list.pop(self.length() - 1)
            # temp = self.list[0]
            # self.list.pop(0)
            return temp
        else:
            raise ValueError
        


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
