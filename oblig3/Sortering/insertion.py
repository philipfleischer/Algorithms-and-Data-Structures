def sort(A):
    n = len(A)
    for i in range(1, n):
        j = i
        while j > 0 and A[j-1] > A[j]:
            #array[j-1], array[j] = array[j], array[j-1]
            A.swap(j, j-1)
            j = j-1

    return A

# Kjøretidskompleksitet: O(n^2)