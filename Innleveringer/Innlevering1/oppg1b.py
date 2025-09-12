from pathlib import Path
import sys
"""
To test the program:
python3 oppg1.py < inputs/eksempel_input
"""

class TreeNode:
    def __init__(self, data: int):
        self._data = data
        self._left = None
        self._right = None
        self._height = 0

    def __repr__(self) -> str:
        return f"TreeNode(data={self._data}, height={self._height}, left_child={self._left._data if self._left else None}, right_child={self._right._data if self._right else None})"

    

class SetAVL:
    def __init__(self) -> None:
        self._root: TreeNode | None = None
        self._size = 0
    
    def contains(self, x: int) -> bool:
        current_node = self._root
        while current_node:
            if current_node._data == x:
                return True
            current_node = current_node._left if x < current_node._data else current_node._right
        return False
    
    def insert(self, x: int) -> TreeNode:
        self._root = self._insert(self._root, x)
    
    def _insert(self, tree_node: TreeNode, x: int) -> TreeNode:
        if not tree_node:
            tree_node = TreeNode(x)
            self._size += 1
            return tree_node
        if tree_node._data < x:
            tree_node._right = self._insert(tree_node._right, x)
        elif tree_node._data > x:
            tree_node._left = self._insert(tree_node._left, x)
        else:
            return tree_node
        self._update_height(tree_node)
        return self._balancing(tree_node)
        

    def size(self) -> int:
        return self._size
    
    def remove(self, x: int) -> None:
        self._root = self._remove(self._root, x)
    
    def _remove(self, tree_node: TreeNode, x: int) -> TreeNode:
        if not tree_node:
            return None
        if tree_node._data < x:
            tree_node._right = self._remove(tree_node._right, x)
        elif tree_node._data > x:
            tree_node._left = self._remove(tree_node._left, x)
        else:
            #Delete the tree_node here:
            if not tree_node._left and not tree_node._right:
                self._size -= 1
                return None
            if not tree_node._left:
                self._size -= 1
                return tree_node._right
            if not tree_node._right:
                self._size -= 1
                return tree_node._left
            child = tree_node._right
            while child._left:
                child = child._left
            tree_node._data = child._data
            tree_node._right = self._remove(tree_node._right, child._data)
        self._update_height(tree_node)
        return self._balancing(tree_node)


    def _find_min_node(self, tree_node: TreeNode) -> TreeNode:
        current_node = tree_node
        while tree_node._left:
            current_node = current_node._left
        return current_node


    def _height(self, tree_node: TreeNode) -> int:
        return tree_node._height if tree_node else -1

    def _update_height(self, tree_node: TreeNode) -> None:
        tree_node._height = 1 + max(self._height(tree_node._left), self._height(tree_node._right))


    def _left_rotate(self, tree_node: TreeNode) -> TreeNode:
        child_node_right = tree_node._right
        child_right_left = child_node_right._left

        child_node_right._left = tree_node
        tree_node._right = child_right_left

        self._update_height(tree_node)
        self._update_height(child_node_right)
        return child_node_right


    def _right_rotate(self, tree_node: TreeNode) -> TreeNode:
        #child_node_left = tree_node._left
        #child_left_right = child_node_left._right

        #child_node_left = tree_node
        #tree_node = child_left_right

        #self._update_height(tree_node)
        #self._update_height(child_node_left)

        #return child_node_left

        x = tree_node._left
        T2 = x._right

        x._right = tree_node
        tree_node._left = T2
        self._update_height(tree_node)
        self._update_height(x)
        return x
    
    def _balance_factor(self, tree_node: TreeNode) -> int:
        if not tree_node:
            return 0
        return self._height(tree_node._left) - self._height(tree_node._right)
    
    def _balancing(self, tree_node: TreeNode) -> TreeNode:
        balance_fact = self._balance_factor(tree_node)
        if balance_fact < -1: #Right heavy
            if self._balance_factor(tree_node._right) > 0:
                tree_node._right = self._right_rotate(tree_node._right)
            return self._left_rotate(tree_node)
        if balance_fact > 1: #Left heavy
            if self._balance_factor(tree_node._left) < 0:
                tree_node._left = self._left_rotate(tree_node._left)
            return self._right_rotate(tree_node)
        return tree_node
    
    def __repr__(self) -> str:
        if not self._root:
            return "SetAVL(empty)"
        
        lines: list[str] = []

        def traverse(tree_node: TreeNode, depth: int = 0, side: str = "root"):
            indent = "  " * depth
            lines.append(f"{indent}{side}: {tree_node._data} (h={tree_node._height})")
            if tree_node._left:
                traverse(tree_node._left, depth + 1, "L")
            if tree_node._right:
                traverse(tree_node._right, depth + 1, "R")

        traverse(self._root)
        return "SetAVL(\n" + "\n".join(lines) + "\n)"
    
    #Reused from oppg1a.py
    def print_tree_ascii(self) -> None:
        root = self._root
        """print tree horizontally with ASCII-branches."""
        def data(n): return getattr(n, "data", getattr(n, "_data", None))
        def left(n): return getattr(n, "left", getattr(n, "_left", None))
        def right(n): return getattr(n, "right", getattr(n, "_right", None))

        def _print(node, prefix="", is_leaf=True):
            if node is None:
                return
            connector = "└── " if is_leaf else "├── "
            print(prefix + connector + str(data(node)))
            children = [c for c in (left(node), right(node)) if c is not None]
            for i, child in enumerate(children):
                last = (i == len(children) - 1)
                _print(child, prefix + ("    " if is_leaf else "│   "), last)

        if root is None: print("(Tree is empty)")
        else: _print(root)



def file_to_SetAVL(filename: str, bst: SetAVL) -> None:
        with open(filename, "r") as f:
            iterations = int(f.readline())
            for _ in range(iterations):
                line = f.readline()
                line_split = line.strip().split(" ")
                if line_split[0] == "contains": print("true" if bst.contains(int(line_split[1])) else "false")
                elif line_split[0] == "insert": bst.insert(int(line_split[1]))
                elif line_split[0] == "remove": bst.remove(int(line_split[1]))
                elif line_split[0] == "size": print(bst.size())
                else: pass


def main():
    my_setavl = SetAVL()
    #file = sys.stdin.read().strip().split()
    base = Path(__file__).parent
    arg = sys.argv[1]
    path = Path(arg)
    if not path.is_absolute():
        path = base / path
    file_to_SetAVL(str(path), my_setavl)
    #print("\nPrinting SetAVL structure using ASCII values to terminal:\n")
    #my_setavl.print_tree_ascii()



if __name__ == "__main__":
    main()