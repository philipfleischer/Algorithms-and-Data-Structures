# skal lese inn filnavn fra bruker og gjøre algoritmene

#Det eneste elementet på første linje av input er hvilken node som katten sitter på
#Det første elementet av hver linje er foreldrenoden, og alle elementene etter er barn mellom verdeiene 1-100
#Det eneste elementet på siste linje er '-1', som signaliserer slutten på treet


#Jeg må altså lage et binært søketre(?) der jeg setter inn verdiene, med riktige relasjoner
#   Etter dette må jeg søke meg frem til noden med verdi lik første element i første linje av input og deretter 
#       Kalle element.parent() til vi kommer til roten, verdiene vi har vært innom skal legges inn i en liste og til
#           slutt skrives ut. Dette er altså stien katten skal følge for å komme seg ned


import sys

class tre:
    def __init__(self, data):
        self.data = data
        self.forelder = None
        self.children = []

def lag_tre():
    #Lager en ordbok for foreldre og deres barn
    noder = {}
    katt = input().strip()

    for linje in sys.stdin:
        linje = linje.strip()
        if linje == "-1":
            break

        #Deler opp linjen i foreldre og barn
        verdier = linje.split()
        forelder_verdi = verdier[0]
        barn_verdi = verdier[1:]

        #sjekker om forelderen finnes i ordboken
        if forelder_verdi not in noder:
            forelder_node = tre(forelder_verdi)
            noder[forelder_verdi] = forelder_node
        else:
            forelder_node = noder[forelder_verdi]

        for barnet in barn_verdi:
            if barnet not in noder:
                barne_node = tre(barnet)
                noder[barnet] = barne_node
            else:
                barne_node = noder[barnet]

                    
            barne_node.forelder = forelder_node
            forelder_node.children.append(barne_node)

    return noder[katt], noder
    

def finn_sti(node):
    sti = []
    midlertidig_node = node
    while midlertidig_node is not None:
        sti.append(midlertidig_node.data)
        midlertidig_node = midlertidig_node.forelder

    return sti
    


def main():
    katt, noder = lag_tre()
    sti = finn_sti(katt)
    print(*sti)

if __name__ == "__main__":
    main()
    





