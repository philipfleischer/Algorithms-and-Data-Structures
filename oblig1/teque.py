# deque --> double-ended queue (dobelt lenket liste)
# teque --> triple-ended queue (trippel lenket liste)
#Teque støtter innsetting på starten, i midten og på slutten av en liste
#Teque skal ha disse funksjonene:
    #push_back(x): Sett elementet x inn bakerst i køen
    #push_front(x): Sett elementet x inn fremst i køen
    #push_middle(x): Sett elementet x inn i midten av køen. midt = (k+1) / 2
    #get(i)): Printer ut det i-te elementet i køen


class Node():
    def __init__(self, data):
        self.data = data
        self.neste = None
        self.forrige = None


class Teque():
    def __init__(self):
        self.start = None
        self.siste = None
        self.stoerrelse = 0

    def push_back(self, data):
        ny_node = Node(data)
        if self.start is None:
            self.start = ny_node
            self.siste = ny_node
        else:
            self.siste.neste = ny_node
            ny_node.forrige = self.siste
            self.siste = ny_node
        self.stoerrelse += 1
  
    
    def push_front(self, data):
        ny_node = Node(data)
        ny_node.neste = self.start
        if self.start is not None:
            self.start.forrige = ny_node
        self.start = ny_node
        if self.siste is None:
                self.siste = ny_node
        self.stoerrelse += 1

    
    def push_middle(self, data):
        ny_node = Node(data)

        if self.start is None:
            self.start = ny_node
            self.siste = ny_node
        else:
            midtpunkt = (self.stoerrelse + 1) // 2
            if midtpunkt == 0:
                self.push_front(data)
            else:
                midl_node = self.get(midtpunkt)
                venstre_midl_node = midl_node.forrige

                if venstre_midl_node is not None:
                    venstre_midl_node.neste = ny_node
                    ny_node.forrige = venstre_midl_node
                else:
                    self.start = ny_node

                ny_node.neste = midl_node
                midl_node.forrige = ny_node
        self.stoerrelse += 1


    def get(self, i):
        if i < self.stoerrelse // 2:
            teller = 0
            midl_node = self.start
            while midl_node is not None:
                if teller == i:
                    return midl_node
                midl_node = midl_node.neste
                teller += 1
        else:
            teller = self.stoerrelse - 1
            midl_node = self.siste
            while midl_node is not None:
                if teller == i:
                    return midl_node
                midl_node = midl_node.forrige
                teller -= 1
        
        return None





#Filstien min: /Users/bruker/Desktop/PROSA/h24/IN2010/oblig1/inputs/eksempel_input
tre_liste = Teque()

fil_sti = input("Vennligst skriv inn fil-stien til input filen din: \n")
with open(fil_sti, "r") as fil:

    #For å hoppe over første linjen i filen
    next(fil)
    for linje in fil:
        #linje = fil.readline()
        linje_stykke = linje.strip().split(" ")
        kommando = linje_stykke[0]
        tall = int(linje_stykke[1])

        if kommando == "push_front":
            tre_liste.push_front(tall)
        elif kommando == "push_back":
            tre_liste.push_back(tall)
        elif kommando == "push_middle":
            tre_liste.push_middle(tall)
        elif kommando == "get":
            node = tre_liste.get(tall) 
            if node is not None:
                print(node.data)
            else:
                print("Noden er tom")
        else:
            print("Noe gikk galt, vennligst prøv igjen")



