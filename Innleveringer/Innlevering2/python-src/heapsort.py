from countcompares import *
from countswaps import *


def heapsort(A: CountSwaps):
    """
    Heapsort time complexity: O(n*log(n))
    """
    arr_length = len(A)

    def heapify(start: int, end: int):
        root = start
        while True:
            child = 2 * root + 1  # LEFT index
            if child > end:
                break
            # Pick larger child
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            # If root < child: swap
            if A[root] < A[child]:
                A.swap(root, child)
                root = child
            else:
                return

    for start in range((arr_length - 2) // 2, -1, -1):
        heapify(start, arr_length - 1)

    for end in range(arr_length - 1, 0, -1):
        A.swap(0, end)
        heapify(0, end - 1)
