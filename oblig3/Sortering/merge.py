# MergeSort-prosedyre: deler listen i to, sorterer og slår sammen
#ENDRA 3 merge_sort ---> sort
def sort(A):
    n = len(A)
    
    # Basistilfelle: en tom eller én element liste er sortert
    if n <= 1:
        return A

    # Del listen i to deler
    mid = n // 2
    #Sorter de to delene
    A1 = sort(A[:mid])
    A2 = sort(A[mid:])

    return merge(A1, A2)
    

#Kombinerer to sorterte lister til en sortert liste
def merge(A1, A2):
    result = []
    i = j = 0 

    #Flett A1 og A2 ved å sammenligne elementene
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            result.append(A1[i])
            i += 1
        else:
            result.append(A2[j])
            j += 1

    #Hvis det er flere elementer igjen i A1, legg dem til resultatet
    while i < len(A1):
        result.append(A1[i])
        i += 1

    while j < len(A2):
        result.append(A2[j])
        j += 1

    return result
