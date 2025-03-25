"""
This module is a test module for the linked_list module.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import unittest

from linked_list_fn import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    Unit tests for the LinkedList class.
    """

    def setUp(self) -> None:
        """
        Set up a fresh LinkedList instance before each test.
        """
        self.ll = LinkedList()

    def test_empty_list(self) -> None:
        """
        Test that an empty list has size 0 and no first or last elements.
        """
        self.assertTrue(self.ll.is_empty())
        self.assertEqual(self.ll.get_size(), 0)
        self.assertIsNone(self.ll.get_first())
        self.assertIsNone(self.ll.get_last())

    def test_add_first(self) -> None:
        """
        Test adding an element at the beginning of the list.
        """
        self.ll.add_first(10)
        self.assertEqual(self.ll.get_first(), 10)
        self.assertEqual(self.ll.get_last(), 10)
        self.assertEqual(self.ll.get_size(), 1)

    def test_add_last(self) -> None:
        """
        Test adding an element at the end of the list.
        """
        self.ll.add_last(20)
        self.assertEqual(self.ll.get_first(), 20)
        self.assertEqual(self.ll.get_last(), 20)
        self.assertEqual(self.ll.get_size(), 1)

    def test_insert(self) -> None:
        """
        Test inserting an element at a specific index.
        """
        self.ll.add_last(1)
        self.ll.add_last(3)
        self.ll.insert(1, 2)
        self.assertEqual(self.ll.get(0), 1)
        self.assertEqual(self.ll.get(1), 2)
        self.assertEqual(self.ll.get(2), 3)

    def test_remove_first(self) -> None:
        """
        Test removing the first element of the list.
        """
        self.ll.add_last(5)
        self.ll.add_last(10)
        self.assertEqual(self.ll.remove_first(), 5)
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll.get_first(), 10)

    def test_remove_last(self) -> None:
        """
        Test removing the last element of the list.
        """
        self.ll.add_last(5)
        self.ll.add_last(10)
        self.assertEqual(self.ll.remove_last(), 10)
        self.assertEqual(self.ll.get_size(), 1)
        self.assertEqual(self.ll.get_last(), 5)

    def test_remove_at(self) -> None:
        """
        Test removing an element at a specific index.
        """
        self.ll.add_last(1)
        self.ll.add_last(2)
        self.ll.add_last(3)
        self.assertEqual(self.ll.remove_at(1), 2)
        self.assertEqual(self.ll.get_size(), 2)
        self.assertEqual(self.ll.get(1), 3)

    def test_contains(self) -> None:
        """
        Test checking if the list contains a certain element.
        """
        self.ll.add_last(100)
        self.assertTrue(self.ll.contains(100))
        self.assertFalse(self.ll.contains(200))

    def test_clear(self) -> None:
        """
        Test clearing the list.
        """
        self.ll.add_last(1)
        self.ll.add_last(2)
        self.ll.clear()
        self.assertTrue(self.ll.is_empty())
        self.assertEqual(self.ll.get_size(), 0)

    def test_iteration(self) -> None:
        """
        Test iterating over the linked list using the iterator.
        """
        self.ll.add_last(10)
        self.ll.add_last(20)
        self.ll.add_last(30)
        elements = [elem for elem in self.ll]  # noqa: C416
        self.assertEqual(elements, [10, 20, 30])


if __name__ == "__main__":
    unittest.main()
