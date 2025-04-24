class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root  # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:  # element matches current.element
                return True  # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
            self.root = self.createNewNode(e)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node not inserted

            newNode = self.createNewNode(e)

            newNode.parent = parent  # Set the parent of the new node

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = newNode
            else:
                parent.right = newNode

        self.size += 1  # Increase tree size
        return True  # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def getSize(self):
        return self.size

    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element, end=" ")
            self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element, end=" ")

    # Preorder traversal from the root
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
        if root != None:
            print(root.element, end=" ")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element
    def path(self, e):
        list = []
        current = self.root  # Start from the root

        while current != None:
            list.append(current)  # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        if current == None and e not in list:
            return []

        return list  # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree
    def delete(self, e):
        current = self.getNode(e)  # Locate node to delete

        if current is None:
            return False  # Element is not in the tree

        # Replace one subtree as a child of its parent with another subtree
        def transplant(u, v):
            if u.parent is None:
                self.root = v  # u is root
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v:
                v.parent = u.parent  # Update parent pointer of v

        if current.left is None:
            transplant(current, current.right)
        elif current.right is None:
            transplant(current, current.left)
        else:
            # Node has two children. Find in-order predecessor (max in left subtree)
            successor = current.left
            while successor.right:
                successor = successor.right
            if successor.parent != current:
                transplant(successor, successor.left)
                successor.left = current.left
                if successor.left:
                    successor.left.parent = successor
            transplant(current, successor)
            successor.right = current.right
            if successor.right:
                successor.right.parent = successor

        self.size -= 1
        return True  # Element deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root = None
        self.size = 0
        return True

    # Return the root of the tree
    def getRoot(self):
        return self.root

    def getNode(self, element):
        current = self.root
        while current:
            if element < current.element:
                current = current.left
            elif element > current.element:
                current = current.right
            else:
                return current
        return None

    # Check if the node with given element is a leaf
    def isLeaf(self, element):
        node = self.getNode(element)
        return node is not None and node.left is None and node.right is None


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None
        self.parent = None  # Point to the parent node, default None


if __name__ == "__main__":
    # Test the BST class
    bst = BST()
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(14)
    bst.insert(4)
    bst.insert(7)
    bst.insert(13)

    print("-" * 50)
    print("Inorder traversal:")
    bst.inorder()  # Output: 1 3 4 6 7 8 10 13 14
    print("\nSize of the tree:", bst.getSize())  # Output: Size of the tree: 9

    print("-" * 50)
    print("Search for 6:", bst.search(6))  # Output: Search for 6: True
    print("Search for 15:", bst.search(15))  # Output: Search for 15: False
    print("Path to 6:", [node.element for node in bst.path(6)])  # Output: Path to 6: [8, 3, 6]

    print("-" * 50)
    print("Deleting 3...")
    bst.delete(3)
    print("Inorder traversal after deleting 3:")
    bst.inorder()  # Output: 1 4 6 7 8 10 13 14
    print("\nSize of the tree after deletion:", bst.getSize())  # Output: Size of the tree after deletion: 8
    print("-" * 50)

    print("Is 3 a leaf?", bst.isLeaf(3))  # Output: Is 3 a leaf? False
    print("Is 13 a leaf?", bst.isLeaf(13))  # Output: Is 13 a leaf? True
    print("-" * 50)

    print("Is the tree empty?", bst.isEmpty())  # Output: Is the tree empty? False
    print("Size of the tree:", bst.getSize())  # Output: Size of the tree: 8
    print("-" * 50)

    print("Clearing the tree...")
    bst.clear()  # Clear the tree
    print("Size of the tree after clearing:", bst.getSize())  # Output: Size of the tree after clearing: 0
    print("Is the tree empty?", bst.isEmpty())  # Output: Is the tree empty? True
    print("-" * 50)
