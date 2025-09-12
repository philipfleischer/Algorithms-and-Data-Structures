from pathlib import Path
import sys

class TreeNode:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None


class SetBST():
    def __init__(self):
        self._root = None
        self._size = 0
    
    def contains(self, x: int) -> bool:
        current_node = self._root
        while current_node:
            if current_node._data == x:
                return True
            current_node = current_node._left if current_node._data < x else current_node._right
        return False
    
    def insert(self, x: int) -> None:
        current_node = self._root
        while current_node:
            if current_node._data == x:
                return
            elif current_node._data < x:
                current_node = current_node._left
            else:
                current_node._data = current_node._right
        
        #Now we are in a treenode->None
        current_node = TreeNode(x)
        self._size += 1
        return

    def remove(self, x: int) -> None:
        self._root = self._remove_recursive(self._root, x)
        return

    def size(self):
        return self._size
    
    def _remove_recursive(self, tree_node: TreeNode, x: int) -> None:
        if tree_node is None:
            return
        if tree_node._data < x:
            tree_node._left = self._remove_recursive(tree_node._left, x)
        elif tree_node._data > x:
            tree_node._right = self._remove_recursive(tree_node._right, x)
        else:
            # tree_node._data == x
            #Need to check if there are any children
            if tree_node._left is None and tree_node._right is None:
                tree_node = None
                return

            #One child, handle
            if tree_node._left

            #two child, handle
        return
        
    
def main():
    my_setbst = SetBST()
    base = Path(__file__).parent
    arg = sys.argv[1]
    path = Path(arg)
    if not path.is_absolute():
        path = base / path
    pathsss = "/Users/bruker/Desktop/PROSA/h25/IN2010/Innleveringer/Innlevering1/inputs/eksempel_input"
    with open(pathsss, "r") as f:
        firstLine = f.readline()
        for _ in range(int(firstLine)):
            line = f.readline()
            line_split = line.strip().split(" ")
            if line_split[0] == "insert":
                my_setbst.insert(int(line_split[1]))
            elif line_split[0] == "contains":
                print(my_setbst.contains(int(line_split[1])))
            elif line_split[0] == "remove":
                my_setbst.remove(int(line_split[1]))
            elif line_split[0] == "size":
                print(my_setbst.size())
            else:
                pass



if __name__ == "__main__":
    main()
