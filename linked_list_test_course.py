"""
This module is a test module for the linked_list module.

Based on the file provided in the course.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

from linked_list_fn import LinkedList


def test_linked_list() -> None:
    """
    Test function for the LinkedList class
    """
    ll = LinkedList()
    # Test add_first og_last
    ll.add_first(1)
    ll.add_last(2)
    ll.add_last(3)
    print("List after adding elements:", ll)
    # Test get_first og get_last
    print("First element:", ll.get_first())
    print("Last element:", ll.get_last())
    # Test insert
    ll.insert(1, 1.5)
    print("List after inserting 1.5 at index 1:", ll)
    # Test remove_first og remove_last
    ll.remove_first()
    print("List after removing first element:", ll)
    ll.remove_last()
    print("List after removing last element:", ll)
    # Test remove_at
    ll.remove_at(1)
    print("List after removing element at index 1:", ll)
    # Test contains
    print("List contains 2:", ll.contains(2))
    print("List contains 3:", ll.contains(3))
    # Test get
    print("Element at index 0:", ll.get(0))
    # Test index_of og last_index_of
    ll.add_last(2)
    ll.add_last(2)
    print("List after adding more 2s:", ll)
    print("Index of first 2:", ll.index_of(2))
    print("Index of last 2:", ll.last_index_of(2))
    # Test set
    ll.set(1, 4)
    print("List after setting index 1 to 4:", ll)
    # Test clear
    ll.clear()
    print("List after clearing:", ll)
    # Test is_empty og get_size
    print("List is empty:", ll.is_empty())
    print("Size of list:", ll.get_size())


if __name__ == "__main__":
    test_linked_list()
