class BinarySearchTree:
    class Node:
        def __init__(self, element):
            self.element = element
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, node, x):
        if node is None:
            return self.Node(x)
        elif x < node.element:
            node.left = self._insert(node.left, x)
        elif x > node.element:
            node.right = self._insert(node.right, x)
        return node

    def min_height(self, node):
        if node is None:
            return -1
        return 1 + min(self.min_height(node.left), self.min_height(node.right))

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self):
        return self.height(self.root) - self.min_height(self.root) <= 1


def main():
    tree = BinarySearchTree()

    try:
        while True:
            line = input() 
            if line == "":
                break
            x = int(line)
            tree.insert(x)
    except EOFError:
        pass

    if tree.is_balanced():
        print("Dette treet ser balansert ut!")
    else:
        print("Dette treet ser ikke helt balansert ut... prøv igjen!")



main()