from countcompares import *
from countswaps import *


def sort(A: CountSwaps):
    """
    Insertion sort implementation using "countswaps" swaping function to count swaps.
    Insertion sort time complexity: O(n^2)
    """
    arr_len = len(A)
    for element in range(1, arr_len):
        cur_element = element
        # Moving A[cur_element] left by switching with neghbour as long as A[cur_element] < A[cur_element - 1]
        while cur_element > 0 and A[cur_element] < A[cur_element - 1]:
            A.swap(cur_element, cur_element - 1)
            cur_element -= 1

    return A
