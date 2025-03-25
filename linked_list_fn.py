"""
This module is an implementation of a linked list.

Based on the file provided in the course.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

from typing import Any


class LinkedList:
    """
    A linked list implementation
    """

    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size = 0

    def get_first(self) -> Any:
        """
        Return the first element in the list
        """
        if not self._head or self._size == 0:
            return None

        return self._head.element

    def get_last(self) -> Any:
        """
        Return the last element in the list
        """
        if not self._tail or self._size == 0:
            return None

        return self._tail.element

    def add_first(self, e: Any) -> None:
        """
        Add an element to the beginning of the list

        Args:
            - e: The element to add
        """
        new_node = Node(e)  # Create a new node
        new_node.next = self._head  # link to "what was first"
        self._head = new_node  # head points to the new node
        self._size += 1  # Increase list size

        if self._tail is None:  # the new node is the only node in list
            self._tail = self._head

    def add_last(self, e: Any) -> None:
        """
        Add an element to the end of the list

        Args:
            - e: The element to add
        """

        new_node = Node(e)  # Create a new node for e

        if self._tail is None:
            self._head = self._tail = new_node  # The only node in list
        else:
            self._tail.next = new_node  # Link the new with the last node
            self._tail = self._tail.next  # tail now points to the last node

        self._size += 1  # Increase size

    def add(self, e: Any) -> None:
        """
        Add an element to the list
        """
        self.add_last(e)

    def insert(self, index: int, e: Any) -> None:
        """
        Insert a new element at the specified index in this list

        Args:
            - index: The index for the new element
            - e: The element to insert
        """
        if index == 0:
            self.add_first(e)  # Insert first
        elif index >= self._size:
            self.add_last(e)  # Insert last
        else:  # Insert in the middle
            current = self._head
            for _ in range(1, index):
                if current:
                    current = current.next

            if current is None:
                raise IndexError("Index out of range")

            temp = current.next
            current.next = Node(e)
            current.next.next = temp
            self._size += 1

    def remove_first(self) -> Any:
        """
        Remove the first node and return the object that is contained in the removed node
        """
        if not self._head or self._size == 0:
            return None  # Nothing to delete
        else:
            temp = self._head  # Keep the first node temporarily
            self._head = self._head.next  # Move head to point the next node
            self._size -= 1  # Reduce size by 1
            if self._head is None:
                self._tail = None  # List becomes empty
            return temp.element  # Return the deleted element

    def remove_last(self) -> Any:
        """
        Remove the last node and return the object that is contained in the removed node
        """
        if not self._head or self._size == 0:
            return None  # Nothing to remove
        elif self._size == 1:  # Only one element in the list
            temp = self._head
            self._head = self._tail = None  # list becomes empty
            self._size = 0
            return temp.element
        else:
            current: Node | None = self._head
            for _ in range(self._size - 2):
                if current:
                    current = current.next

            if current is None or self._tail is None:
                return None

            temp = self._tail
            self._tail = current
            self._tail.next = None
            self._size -= 1
            return temp.element

    def remove_at(self, index: int) -> Any:
        """
        Remove the element at the specified position in this list.
        """
        if index < 0 or index >= self._size:
            return None  # Out of range
        elif index == 0:
            return self.remove_first()  # Remove first
        elif index == self._size - 1:
            return self.remove_last()  # Remove last
        else:
            previous = self._head
            for _ in range(1, index):
                if previous:
                    previous = previous.next

            if previous is None or previous.next is None:
                return None

            current = previous.next
            previous.next = current.next
            self._size -= 1
            return current.element

    def is_empty(self) -> bool:
        """
        Return true if the list is empty
        """
        return self._size == 0

    def get_size(self) -> int:
        """
        Return the size of the list
        """
        return self._size

    def __str__(self) -> str:
        """
        Return a string representation of the list
        """
        result = "["
        current = self._head

        for _ in range(self._size):
            if current is None:
                result += "]"
                break

            result += str(current.element + ", ")
            current = current.next

        return result

    def clear(self) -> None:
        """
        Clear the list
        """
        self._head = self._tail = None
        self._size = 0

    # Return true if this list contains the element e
    def contains(self, e):
        print("Implementation left as an exercise")
        return True

    # Remove the element and return true if the element is in the list
    def remove(self, e):
        print("Implementation left as an exercise")
        return True

    # Return the element from this list at the specified index
    def get(self, index):
        print("Implementation left as an exercise")
        return None

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def index_of(self, e):
        print("Implementation left as an exercise")
        return 0

    # Return the index of the last matching element in this list
    #  Return -1 if no match.
    def last_index_of(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    #  with the specified element.
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None

    # Return elements via indexer, can use list[0] to get the first element etc
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self._head)


class Node:
    """
    A node in a linked list
    """

    def __init__(self, e: Any):
        self.element: Any = e
        self.next: Node | None


class LinkedListIterator:
    """
    An iterator for a linked list
    """

    def __init__(self, head: Node):
        self._current = head

    def __next__(self) -> Any:
        if self._current is None:
            raise StopIteration
        else:
            element = self._current.element
            self._current = self._current.next
            return element
