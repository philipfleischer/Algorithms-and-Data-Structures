class Node:
    def __init__(self, key):
        self.key = key
        self.hoyre = None
        self.venstre = None
        self.hoyde = 1


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
        #Så lenge x ikke finnes i mengden
        if not self.contains(x):
            self.rot = self.hjelp_insert(self.rot, x)
            self.stoerrelse += 1
    
    def hjelp_insert(self, node, x):
        if not node:
            #Der det ikke finnes en node, legger vi til denne noden
            return Node(x)
        
        if x < node.key:
            node.venstre = self.hjelp_insert(node.venstre, x)
        else:
            node.hoyre = self.hjelp_insert(node.hoyre, x)

        #Ender høyde
        node.hoyde = 1 + max(self.finn_hoyde(node.venstre), self.finn_hoyde(node.hoyre))

        #Sjekk om det er balanse eller ikke
        balanse = self.finn_balanse(node)

        #Hvis den er i ubalanse mot venstre-venstre
        if balanse > 1 and x < node.venstre.key:
            return self.hoyre_rotasjon(node)

        #Hvis den er i ubalanse mot hoyre-hoyre
        if balanse < -1 and x > node.hoyre.key:
            return self.venstre_rotasjon(node)
        
        #Hvis den er i ubalanse mot venstre-hoyre
        if balanse > 1 and x > node.venstre.key:
            node.venstre = self.venstre_rotasjon(node.venstre)
            return self.hoyre_rotasjon(node)
        
        #Hvis den er i ubalanse mot hoyre-venstre
        if balanse > -1 and x > node.hoyre.key:
            node.hoyre = self.hoyre_rotasjon(node.hoyre)
            return self.venstre_rotasjon(node)

        #Returnerer node etter eventuell balansering
        return node


    def remove(self, x):
        if self.contains(x):
            self.rot = self.hjelp_remove(self.rot, x)
            self.stoerrelse -= 1


    def hjelp_remove(self, node, x):
        if node is None:
            return
        
        if x < node.key:
            node.venstre = self.hjelp_remove(node.venstre, x)
        elif x > node.key:
            node.hoyre = self.hjelp_remove(node.hoyre, x)
        else:
            if node.venstre is None:
                return node.hoyre
            elif node.hoyre is None:
                return node.venstre
            
            midl = self.minste_node(node.hoyre)
            node.key = midl.key
            node.hoyre = self.hjelp_remove(node.hoyre, midl.key)

        #endrer høyden
        node.hoyde = 1 + max(self.finn_hoyde(node.venstre), self.finn_hoyde(node.hoyre))

        #Sjekk balansen
        balanse = self.finn_balanse(node)

        #Hvis den er i ubalanse mot venstre-venstre
        if balanse > 1 and self.finn_balanse(node.venstre) >= 0:
            return self.hoyre_rotasjon(node)

        #Hvis den er i ubalanse mot hoyre-hoyre
        if balanse < -1 and self.finn_balanse(node.hoyre) <= 0:
            return self.venstre_rotasjon(node)
        
        #Hvis den er i ubalanse mot venstre-hoyre
        if balanse > 1 and self.finn_balanse(node.venstre) < 0:
            node.venstre = self.venstre_rotasjon(node.venstre)
            return self.hoyre_rotasjon(node)
        
        #Hvis den er i ubalanse mot hoyre-venstre
        if balanse > -1 and self.finn_balanse(node.hoyre) > 0:
            node.hoyre = self.hoyre_rotasjon(node.hoyre)
            return self.venstre_rotasjon(node)

        return node
    
    def minste_node(self, node):
        midl = node
        while midl.venstre is not None:
            midl = midl.venstre
        return midl


    def size(self):
        return self.stoerrelse
    

    def finn_hoyde(self, node):
        if not node:
            return 0
        return node.hoyde
    
    def finn_balanse(self, node):
        if not node:
            return 0
        return self.finn_hoyde(node.venstre) - self.finn_hoyde(node.hoyre)
    
    def hoyre_rotasjon(self, node):
        node_venstre = node.venstre
        node_venstre_hoyre = node_venstre.hoyre

        #Rotér
        node_venstre.hoyre = node
        node.venstre = node_venstre_hoyre

        #Høyder
        node.height = 1 + max(self.finn_hoyde(node.venstre), self.finn_hoyde(node.hoyre))
        node_venstre.height = 1 + max(self.finn_hoyde(node_venstre.venstre), self.finn_hoyde(node_venstre.hoyre))

        return node_venstre
    
    def venstre_rotasjon(self, node):
        node_hoyre = node.hoyre
        node_hoyre_venstre = node_hoyre.venstre

        #Rotér
        node_hoyre.venstre = node
        node.hoyre = node_hoyre_venstre

        #Høyder
        node.height = 1 + max(self.finn_hoyde(node.venstre), self.finn_hoyde(node.hoyre))
        node_hoyre.height = 1 + max(self.finn_hoyde(node_hoyre.venstre), self.finn_hoyde(node_hoyre.hoyre))

        return node_hoyre
    




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










