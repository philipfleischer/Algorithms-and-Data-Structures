def partisjon(A, low, high):
    #Pivot som siste element
    pivot = A[high]
    #Indeks for minste
    i = low - 1

    #Sammenlign mot pivot-element
    for j in range(low, high):
        #CountCompares
        if A[j] <= A[high]:
            i += 1
            A.swap(i, j)

    A.swap(i + 1, high)
    return i + 1

def quick_rekursjon(A, low, high):
    if low < high:
        #Partisjonerer for å finne riktig pivot-element
        pivot = partisjon(A, low, high)

        # Sorter begge sider av pivot
        quick_rekursjon(A, low, pivot - 1)
        quick_rekursjon(A, pivot + 1, high)

def sort(A):
    quick_rekursjon(A, 0, len(A) - 1)
    return A