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
    
    def __repr__(self) -> str:
        return f"TreeNode(data={self._data}, left_child={self._left}, right_child={self._right})"
    

class SetBST:
    def __init__(self) -> None:
        self._root: TreeNode | None = None
        self._size = 0
    
    def contains(self, x: int) -> bool:
        current_node = self._root
        while current_node:
            if current_node._data == x: return True
            current_node = current_node._left if x < current_node._data else current_node._right
        return False
    

    def insert(self, x: int) -> None:
        if self._root is None:
            self._root = TreeNode(x)
            self._size += 1
            return
        
        parent = None
        current_node = self._root

        while current_node:
            parent = current_node
            if current_node._data == x:
                return 
            elif current_node._data < x:
                current_node = current_node._right
            else:
                current_node = current_node._left

        new_node = TreeNode(x)
        if parent._data < x:
            parent._right = new_node
        else:
            parent._left = new_node
        self._size += 1
    

    def size(self) -> int:
        return self._size
    
    
    def remove(self, x: int) -> None:
            self._root = self._remove_rec(self._root, x)
            return
        
    
    def _remove_rec(self, tree_node: TreeNode, target: int) -> None:
        if tree_node == None:
            return None

        if tree_node._data > target:
            tree_node._left = self._remove_rec(tree_node._left, target)
            return tree_node
        elif tree_node._data < target:
            tree_node._right = self._remove_rec(tree_node._right, target)
            return tree_node
        
        #x == tree_node._data
        #Need to reduce the size, but not handle children
        #Case 1: 0 children
        if tree_node._left is None and tree_node._right is None:
            self._size -= 1
            return None
        #Case 2: right child remove
        if tree_node._left is None:
            self._size -= 1
            return tree_node._right
        #Case 3: left child remove
        if tree_node._right is None:
            self._size -= 1
            return tree_node._left

        #Case 4: Two children (left and right) remove
        #Now we work on two children
        parent = tree_node
        child = tree_node._right
            
        while child._left:
            parent = child
            child = child._left
        #Copy the value
        tree_node._data = child._data

        #remove parent-treenode
        if parent._left is child:
            parent._left = child._right
        else:
            parent._right = child._right
        self._size -= 1
        return None

    #Made this function to better understand the debugging objects when 'run and debug'-ing
    def __repr__(self) -> str:
        if not self._root:
            return "SetBST(empty SetBST object)"
        
        lines: list[str] = []

        #NOTE: Should i reuse this somewhere else?
        def traverse(node: TreeNode, depth: int = 0, side: str = "root"):
            indent = "  " * depth
            lines.append(f"{indent}{side}: {node.key}")
            if node.left:
                traverse(node.left, depth + 1, "L")
            if node.right:
                traverse(node.right, depth + 1, "R")

        traverse(self._root)
        return "SetBST(\n" + "\n".join(lines) + "\n)"

        

    #Just for fun!
    def print_tree_ascii(self) -> None:
        root = self._root
        """print tree horizontally with ASCII-branches."""
        #getattr() func is used to get and compare attributes
        def data(n): return getattr(n, "data", getattr(n, "_data", None))
        def left(n): return getattr(n, "left", getattr(n, "_left", None))
        def right(n): return getattr(n, "right", getattr(n, "_right", None))

        def _print(node, prefix="", is_leaf=True):
            if node is None:
                return
            connector = "└── " if is_leaf else "├── "
            print(prefix + connector + str(data(node)))
            #add the children (wrote it in a new and interesting compact form)
            children = [c for c in (left(node), right(node)) if c is not None]
            for i, child in enumerate(children):
                last = (i == len(children) - 1)
                _print(child, prefix + ("    " if is_leaf else "│   "), last)

        if root is None: print("(Tree is empty)")
        else: _print(root)



def file_to_SetBST(filename: str, bst: SetBST) -> None:
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
    my_setbst = SetBST()
    #file = sys.stdin.read().strip().split()
    base = Path(__file__).parent
    arg = sys.argv[1]
    path = Path(arg)
    if not path.is_absolute():
        path = base / path
    file_to_SetBST(str(path), my_setbst)
    #print("\nPrinting SetBST structure using ASCII values to terminal:\n")
    #my_setbst.print_tree_ascii()



if __name__ == "__main__":
    main()