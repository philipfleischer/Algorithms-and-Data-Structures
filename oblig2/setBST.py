class Node:
    def __init__(self, key):
        self.key = key
        self.hoyre = None
        self.venstre = None


class Set:
    def __init__(self):
        self.rot = None
        self.stoerrelse = 0

    def contains(self, x):
        midl = self.rot

        while midl:
            if x == midl.key:
                return True
            elif x < midl.key:
                midl = midl.venstre
            else:
                midl = midl.hoyre
        return False
    
    def insert(self, x):
        if self.rot is None:
            self.rot = Node(x)
            self.stoerrelse += 1
            return
       
        midl = self.rot
        forelder = None
        while midl:
            forelder = midl
            #hvis x finnes
            if x == midl.key:
                return
            elif x < midl.key:
                midl = midl.venstre
            else:
                midl = midl.hoyre
       
        if x < forelder.key:
            forelder.venstre = Node(x)
        else:
            forelder.hoyre = Node(x)
        
        self.stoerrelse += 1


    def remove(self, x):
        if self.contains(x):
            self.rot = self.hjelp_remove(self.rot, x)
            self.stoerrelse -= 1


    def hjelp_remove(self, node, x):
        if node is None:
            return None
        
        if x < node.key:
            node.venstre = self.hjelp_remove(node.venstre, x)
        if x > node.key:
            node.hoyre = self.hjelp_remove(node.hoyre, x)
        else:
            if node.venstre is None:
                return node.hoyre
            elif node.hoyre is None:
                return node.venstre
            
            midl = self.minste_node(node.hoyre)
            node.key = midl.key
            node.hoyre = self.hjelp_remove(node.hoyre, midl.key)

        return node
    
    def minste_node(self, node):
        midl = node
        while midl.venstre is not None:
            midl = midl.venstre
        return midl


    def size(self):
        return self.stoerrelse


import sys
input = sys.stdin.read


def main():
    set = Set()

    info = input().splitlines()
    antall_linjer = int(info[0])

    for i in range(1, antall_linjer + 1):
        kommando = info[i].split()

        if kommando[0] == "contains":
            x = int(kommando[1])
            print(set.contains(x))
        elif kommando[0] == "insert":
            x = int(kommando[1])
            set.insert(x)
        elif kommando[0] == "remove":
            x = int(kommando[1])
            set.remove(x)
        elif kommando[0] == "size":
            print(set.size())


main()










