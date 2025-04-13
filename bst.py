"""
This module is an implementation of a binary search tree.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V
"""

from typing import Optional


class BinarySearchTree:
    """
    A binary search tree (BST) implementation.
    """

    def __init__(self) -> None:
        self._root: Node | None = None

    def insert(self, value: int) -> None:
        """
        Insert a value into the BST.
        """
        self._root = self._insert_recursive(self._root, value)

    def _insert_recursive(self, node: Optional["Node"], value: int) -> "Node":
        if node is None:
            return Node(value)

        if node.element and value < node.element:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        return node


class Node:
    """
    A node in a binary search tree.
    """

    def __init__(self, element: int | None = None) -> None:
        self._element: int | None = element
        self._left: Node | None = None
        self._right: Node | None = None

    @property
    def element(self) -> int | None:
        """
        The element stored in this node.
        """
        return self._element

    @element.setter
    def element(self, value: int) -> None:
        self._element = value

    @property
    def left(self) -> Optional["Node"]:
        """
        The left child of this node.
        """
        return self._left

    @left.setter
    def left(self, value: Optional["Node"]) -> None:
        self._left = value

    @property
    def right(self) -> Optional["Node"]:
        """
        The right child of this node.
        """
        return self._right

    @right.setter
    def right(self, value: Optional["Node"]) -> None:
        self._right = value

    def __str__(self) -> str:
        return f"Node = {self._element}"


if __name__ == "__main__":
    print("Hello")

    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)

    print(bst._root)
