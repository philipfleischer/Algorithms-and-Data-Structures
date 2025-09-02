import sys
"""
To test the program:
python3 oppg1.py < inputs/eksempel_input
"""

"""
TODO: Have to make a Node class?
how do i do that when working with a set
TODO: Have to:
"""

class Node:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
    

class SetBST:
    def __init__(self) -> None:
        self._my_set = set()
        self._readFile(sys.stdin.readline())

    
    def _readFile(self, filename: str) -> None:
        print("1")
        with open(filename, "r") as f:
            for line in f:
                line_split = line.strip().split(" ")
                if type(line_split[0]) is isinstance(int):
                    # Count of number of operations to be done
                    pass
                if line_split[0] == "contains":
                    print(contains(my_set(), line_split[1]))
                if line_split[0] == "insert":
                    pass
                if line_split[0] == "remove":
                    pass
                if line_split[0] == "size":
                    pass

    
    def contains(self, mengde: set, x: int) -> bool:
        low = 0
        high = len(mengde) - 1
        while low <= high:
            print("WE GET HERE")
            i = (low + high) / 2
            if mengde[i] == x:
                return true
            elif mengde[i] < x:
                low = i + 1
            elif mengde[i] > x:
                high = i - 1
        return false

    def insert(self, v: int, x: int) -> None:
        #v is a Node, x is an element
        if not contains(v):
            v = Node(x)
        elif x < v.element:
            v.left = insert(v.left, x)
        elif x > v.element:
            v.right = insert(v.right, x)
        return v
    
    def remove(self, v: int, x: int) -> None:
        #v is a Node, x is an element
        pass

    def size(self, mySet: set) -> int:
        #return the size of the set in O(1)
        pass



def main():
    my_setbst = SetBST()
    print("END")


main()