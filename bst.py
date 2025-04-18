class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root  # Start from the root

        while current is not None:
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
        if self.root is None:
            self.root = self.create_new_node(e)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current is not None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.create_new_node(e)
            else:
                parent.right = self.create_new_node(e)

        self.size += 1  # Increase tree size
        return True  # Element inserted

    # Create a new TreeNode for element e
    def create_new_node(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def get_size(self):
        return self.size

    # Inorder traversal from the root
    def inorder(self):
        self.inorder_helper(self.root)

    # Inorder traversal from a subtree
    def inorder_helper(self, r):
        if r is not None:
            self.inorder_helper(r.left)
            print(r.element, end=" ")
            self.inorder_helper(r.right)

    # Postorder traversal from the root
    def postorder(self):
        self.postorder_helper(self.root)

    # Postorder traversal from a subtree
    def postorder_helper(self, root):
        if root is not None:
            self.postorder_helper(root.left)
            self.postorder_helper(root.right)
            print(root.element, end=" ")

    # Preorder traversal from the root
    def preorder(self):
        self.preorder_helper(self.root)

    # Preorder traversal from a subtree
    def preorder_helper(self, root):
        if root is not None:
            print(root.element, end=" ")
            self.preorder_helper(root.left)
            self.preorder_helper(root.right)

    # Returns a path from the root leading to the specified element
    def path(self, e):
        list = []
        current = self.root  # Start from the root

        while current is not None:
            list.append(current)  # Add the node to the list
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                break

        return list  # Return an array of nodes

    # Delete an element from the binary search tree.
    # Return True if the element is deleted successfully
    # Return False if the element is not in the tree
    def delete(self, e):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current is not None:
            if e < current.element:
                parent = current
                current = current.left
            elif e > current.element:
                parent = current
                current = current.right
            else:
                break  # Element is in the tree pointed by current

        if current is None:
            return False  # Element is not in the tree

        # Case 1: current has no left children
        if current.left is None:
            # Connect the parent with the right child of the current node
            if parent is None:
                self.root = current.right
            else:
                if e < parent.element:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the right_most node in the left subtree of
            # the current node and also its parent
            parent_of_right_most = current
            right_most = current.left

            while right_most.right is not None:
                parent_of_right_most = right_most
                right_most = right_most.right  # Keep going to the right

            # Replace the element in current by the element in right_most
            current.element = right_most.element

            # Eliminate right_most node
            if parent_of_right_most.right == right_most:
                parent_of_right_most.right = right_most.left
            else:
                # Special case: parent_of_right_most == current
                parent_of_right_most.left = right_most.left

        self.size -= 1
        return True  # Element deleted

    # Return true if the tree is empty
    def is_empty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def get_root(self):
        return self.root


class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None
