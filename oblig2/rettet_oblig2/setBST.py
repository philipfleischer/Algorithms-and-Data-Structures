import sys
# Lag et binært søke-tre
#

class Node():
    def __init__(self, key):
        self.key = key
        self.venstre = None
        self.hoyre = None


class Set():
    def __init__(self):
        self.rot = None
        self.stoerrelse = 0

    def contains(self, data):
        midl_node = self.rot

        while midl_node is not None:
            if midl_node == data:
                return True
            elif midl_node < data:
                midl_node = midl_node.venstre
            else:
                midl_node = midl_node.hoyre
        return False
    
    def insert(self, data):
        if self.rot is None:
            self.rot = Node(data)
            self.stoerrelse += 1
            return

        midl_node = self.rot
        forelder = None

        while midl_node is not None:
            forelder = midl_node
            #Duplikat?
            if midl_node == data:
                return 
            elif midl_node < data:
                midl_node = midl_node.venstre
            else:
                midl_node = midl_node.hoyre
        
        if data < forelder.key:
            forelder.venstre = Node(data)
        else:
            forelder.hoyre = Node(data)

        self.stoerrelse += 1

    def minste_node(self, node):
        midl_node = node

        while midl_node.venstre is not None:
            midl_node = midl_node.venstre
        return midl_node
    

    def remove(self, data):
        if self.contains(data):
            self.rot = self.hjelp_remove(self.rot, data)
            #self.stoerrelse -= 1


    def hjelp_remove(self, node, data):
        if node is None:
            return
        
        if data < node.key:
            node.venstre = self.hjelp_remove(node.venstre, data)
        if data > node.key:
            node.hoyre = self.hjelp_remove(node.hoyre, data)
        else:
            if node.venstre is None:
                return node.hoyre
            elif node.hoyre is None:
                return node.venstre
            
            midl = self.minste_node(node.hoyre)
            node.key = midl.key
            node.hoyre = self.hjelp_remove(node.hoyre, midl.key)

        #Skal denne være her?
        self.stoerrelse -= 1
        return node
    
    def size(self):
        return self.stoerrelse
    



def main():
    set = Set()
    input = sys.stdin.read

    deler = input().splitlines()
    antall_linjer = int(deler[0])

    for i in range(1, antall_linjer + 1):
        kommando = deler[i].split()

        if kommando[0] == "contains":
            x = int(kommando[1])
            if set.contains(x):
                print("true")
            else:
                print("false")

        elif kommando[0] == "insert":
            x = int(kommando[1])
            set.insert(x)

        elif kommando[0] == "remove":
            x = int(kommando[1])
            set.remove(x)

        elif kommando[0] == "size":
            print(set.size())

        


if __name__ == "__main__":
    main()