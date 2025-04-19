from BST import BST


class BSTIterator:
    def __init__(self, bst: BST):
        self.stack = []  # Stack to store the nodes
        self.current = bst.getRoot()  # Start from the root

    def __iter__(self):
        return self

    def has_next(self):
        return self.current is not None or len(self.stack) > 0

    def __next__(self):
        while self.has_next():
            if self.current is not None:  # if current node is not None
                self.stack.append(self.current)  # Add current node to stack
                self.current = self.current.left  # Move to the left child
            else:  # if current node is None
                self.current = self.stack.pop()  # Pop the last node from stack
                result = self.current.element  # Get the element of the current node
                self.current = self.current.right  # Move to the right child
                return result  # Return the element of the current node

        raise StopIteration  # No more elements in the tree


class MyBST(BST):
    def __iter__(self):
        return BSTIterator(self)  # Return an iterator for the tree

    def __len__(self):
        return self.size  # Return the size of the tree

    def __max__(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.element

    def __min__(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.element

    def __sum__(self):
        total = 0
        for element in self:
            total += element
        return total

    def __set__(self, instance, value):
        return set(self)

    def __list__(self):
        return list(self)


def main():
    tree = MyBST()

    s = input("Enter integers in one line for tree separated by space: ")

    list1 = [int(x) for x in s.split()]

    for e in list1:
        tree.insert(e)

    print(s, "are inserted into the tree")
    print("In-order traverse should give sorted order: ", end="")

    iterator = iter(tree)  # Create an iterator

    try:
        while True:
            print(next(iterator), end=" ")
    except StopIteration:
        print("All traversed")

    print("Max element:", max(tree))  # Print the max element in the tree
    print("Min element:", min(tree))  # Print the min element in the tree
    print("Sum:", sum(tree))  # Print the sum of all elements in the tree
    print("Set:", set(tree))  # Print the set
    print("List:", list(tree))  # Print the list


if __name__ == "__main__":
    main()
