from typing import List, TypeVar

T = TypeVar("T")

def binary_search(arr: List[T], target: T) -> bool:
    """Time complexity: O(log(n)). """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 # -> // floor division operator

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return False

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)
#Out: Target not found in list

result = binary_search(numbers, 6)
verify(result)
#Out: Target at index: 5