from typing import List, TypeVar

T = TypeVar("T")

def recursive_binary_search(arr: List[T], target: T) -> bool:
    if len(arr) == 0:
        return False
    else:
        i = (len(arr)) // 2

        if arr[i] == target:
            return True
        else:
            if arr[i] < target:
                return recursive_binary_search(arr[i + 1:], target)
            if arr[i] > target:
                return recursive_binary_search(arr[:i], target)

#If the left half is too small, we recursively call the function
#We do that from the midpoint + 1 up to the end of the array
#If the left half is too large, we recursively call the function
#We do that from the start up to the midpoint - 1 of the array

#We should not use the recursive function, but rather the iterative 
# function, because the time complexity is O(log(n)) for both, BUT
# the space complexity is O(log(n)) for iterative, but O(n) for 
# recursive.

def verify(result):
    print("Target found: ", result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 6)
verify(result)