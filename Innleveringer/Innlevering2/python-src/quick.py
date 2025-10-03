from countcompares import *
from countswaps import *


def sort(A: CountSwaps) -> CountSwaps:
    """
    Calling the quicksort algorithm.
    Quick sort Time Complexity: O(n^2)
    """
    _quicksort(A, 0, len(A) - 1)

    return A


def _quicksort(A: CountSwaps, low: int, high: int):
    while low < high:
        partition = _get_partition(A, low, high)
        if (partition - 1 - low) < (high - (partition + 1)):
            _quicksort(A, low, partition - 1)
            low = partition + 1
        else:
            _quicksort(A, partition + 1, high)
            high = partition - 1


def _get_partition(A: CountSwaps, low: int, high: int) -> int:
    pivot = A[high]
    pivot_index = low - 1
    for element in range(low, high):
        if A[element] < pivot:
            pivot_index += 1
            if pivot_index != element:
                A.swap(pivot_index, element)

    if pivot_index + 1 != high:
        A.swap(pivot_index + 1, high)

    return pivot_index + 1
