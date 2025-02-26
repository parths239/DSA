class TreeNode:
    """Represents a node in the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation with encapsulated methods."""
    def __init__(self):
        self.root = None

    def add(self, data):
        """Inserts a value into the BST."""
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._add_recursive(self.root, data)

    def _add_recursive(self, node, data):
        """Helper function to insert a node recursively."""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._add_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._add_recursive(node.right, data)

    def search(self, val):
        """Searches for a value in the BST."""
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        """Helper function to search recursively."""
        if node is None:
            return False
        if node.data == val:
            return True
        if val < node.data:
            return self._search_recursive(node.left, val)
        return self._search_recursive(node.right, val)

    def in_order_traversal(self):
        """Returns an in-order traversal (sorted list) of the BST."""
        elements = []
        self._in_order_recursive(self.root, elements)
        return elements

    def _in_order_recursive(self, node, elements):
        """Helper function to perform in-order traversal."""
        if node:
            self._in_order_recursive(node.left, elements)
            elements.append(node.data)
            self._in_order_recursive(node.right, elements)

    def delete(self, val):
        """Deletes a value from the BST."""
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        """Helper function to delete a node recursively."""
        if node is None:
            return None

        if val < node.data:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.data:
            node.right = self._delete_recursive(node.right, val)
        else:  # Node to be deleted found
            # Case 1: Node has no children
            if node.left is None and node.right is None:
                return None
            # Case 2: Node has one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: Node has two children
            min_val = self._find_min(node.right)
            node.data = min_val
            node.right = self._delete_recursive(node.right, min_val)

        return node

    def _find_min(self, node):
        """Finds the minimum value node in a subtree."""
        while node.left:
            node = node.left
        return node.data


# ---------------- Testing the BST ----------------
if __name__ == '__main__':
    bst = BinarySearchTree()

    # Insert elements into BST
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    for el in elements:
        bst.add(el)

    print("In-order traversal:", bst.in_order_traversal())  # Expected: [1, 4, 9, 17, 18, 20, 23, 34]

    # Searching for elements
    print("Searching for 20:", bst.search(20))  # Expected: True
    print("Searching for 100:", bst.search(100))  # Expected: False

    # Deleting elements and checking in-order traversal
    bst.delete(20)
    print("After deleting 20:", bst.in_order_traversal())  # Expected: [1, 4, 9, 17, 18, 23, 34]

    bst.delete(9)
    print("After deleting 9:", bst.in_order_traversal())  # Expected: [1, 4, 17, 18, 23, 34]

    bst.delete(17)
    print("After deleting 17:", bst.in_order_traversal())  # Expected: [1, 4, 18, 23, 34]
