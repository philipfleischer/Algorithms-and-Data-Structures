from countcompares import *
from countswaps import *


def mergesort(A: CountSwaps):
    """
    Top-down mergesort using a buffer; counts moves via assign().
    Mergesort time complexity: O(n*log(n))
    """

    arr_length = len(A)
    if arr_length <= 1:
        return A
    buffer: list = [None] * arr_length

    def merge(low: int, mid: int, high: int):
        for element in range(low, high + 1):
            buffer[element] = A[element]

        cur_low, cur_mid = low, mid + 1
        for element in range(low, high + 1):
            if cur_low > mid:
                A[element] = buffer[cur_mid]
                A.swaps += 1
                cur_mid += 1
            elif cur_mid > high:
                A[element] = buffer[cur_low]
                A.swaps += 1
                cur_low += 1
            else:
                if buffer[cur_mid] < buffer[cur_low]:
                    A[element] = buffer[cur_mid]
                    A.swaps += 1
                    cur_mid += 1
                else:
                    A[element] = buffer[cur_low]
                    A.swaps += 1
                    cur_low += 1

    def sort_rec(low: int, high: int):
        if low >= high:
            return
        mid = (low + high) // 2
        sort_rec(low, mid)
        sort_rec(mid + 1, high)
        if not (A[mid + 1] < A[mid]):
            return
        merge(low, mid, high)

    sort_rec(0, arr_length - 1)
    return A


def sort(A: CountSwaps):
    return mergesort(A)
