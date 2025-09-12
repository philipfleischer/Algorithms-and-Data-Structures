from typing import List, TypeVar
from file_to_list import make_list

T = TypeVar("T")

def binary_search_string(arr: List[T], target: T) -> bool:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
    return mid

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


names: List[T] = make_list("names/sorted.txt")
search_names: List[T] = make_list("Tester/names_smallToo.txt")
for n in search_names:
    index = binary_search_string(names, n)
    print(index)