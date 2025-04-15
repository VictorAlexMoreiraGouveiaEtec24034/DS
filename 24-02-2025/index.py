class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self, value):
        self.root = None

    def insert(self, value):
        if (self.root is None):
            self.root = Node(value)
        
        else:
            _insert(self.root, value)

    def _insert(self, node, value):
        if value < node:
            if node.left is None:
                node.left = Node(value)

            else:
                self._insert(self.node.left, value)

        else:
            if node.right is None:
                node.right = Node(value)

            else:
                self._insert(node.right, value)

    

