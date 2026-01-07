import heapq

#Lager en funksjon som finner midtverdier og legger dem i en heap
def lag_balanse(array):
    heap = []
    
    #Følte dette ble mer oversiktlig?
    def innsetting(lav, hoy):
        if lav > hoy:
            return
        
        #Finner midtverdien og legg den i heapen
        mid = (lav + hoy) // 2
        heapq.heappush(heap, array[mid])
        
        #legger midtverdiene inn rekursivt fra venstre og høyre subarrays
        innsetting(lav, mid - 1)
        innsetting(mid + 1, hoy)

    innsetting(0, len(array) - 1)    
    return heap

# Funksjon som bygger en heap fra en sortert liste og balanserer
def main():
    array = [int(x) for x in input("Skriv inn sorterte heltall, separert med mellomrom: ").split()]
    
    heap = []
    for i in array:
        heapq.heappush(heap, i)
    
    balansert_rekkefolge = lag_balanse(array)
    print(balansert_rekkefolge)

if __name__ == "__main__":
    main()