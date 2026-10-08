# stack.py
# Custom Stack implementation for the expression evaluator
# Student: Joseph Tommy Koroma
# Student ID: 905005353
# Class: DIT1201F

class Stack:
    """A simple Stack data structure that follows LIFO (Last In, First Out)."""

    def __init__(self):
        # Internal list to store stack items
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack.
        Returns None if the stack is empty."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it.
        Returns None if the stack is empty."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items, False otherwise."""
        return len(self._items) == 0

    def __str__(self):
        """Return a string representation of the stack (bottom to top)."""
        return str(self._items)
