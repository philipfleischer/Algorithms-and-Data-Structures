#A - array, n - len(array), i - indeks
#Funksjon som forutsetter at heap egeneskaper blir bevart
def lag_heap(A, n, i):
    low = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] < A[low]:
        low = left

    if right < n and A[right] < A[low]:
        low = right

    if low != i:
        #A[i], A[smallest] = A[smallest], A[i]
        #Bytter plass siden det laveste elementet har blitt oppdatert
        A.swap(i, low)
        #Kaller rekursivt
        lag_heap(A, n, low)

def sort(A):
    n = len(A)

    #Løkke som starter på første element med barn. Fortsetter bakover mot roten
    for i in range(n // 2 - 1, -1, -1):
        #Kaller heap for at det alltid skal være en min-heap
        lag_heap(A, n, i)

    #Løkke der vi bytter minste element med siste element i listen
    for i in range(n - 1, 0, -1):
        #A[i], A[0] = A[0], A[i]
        #Bytter rot-elementet, med siste på heapen (i)
        A.swap(i, 0)
        lag_heap(A, i, 0)
    
    #For å returnere retur med synkende rekkefølge
    return A[::-1]