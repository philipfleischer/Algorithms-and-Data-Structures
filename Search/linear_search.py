#Linear search algorithm:

#Importing this to get generic types
from typing import List, TypeVar
#Now we can pass all types into the linear_search
T = TypeVar("T")

def linear_search(arr: List[T], target: T) -> int | None:
    """The linear-search accepts two arguments: 
    list we are looking through and target value we are looking for.
    Return the position of the target in the list or None.
    Time complexity: O(n). """

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)
#Out: Target not found in list

result = linear_search(numbers, 6)
verify(result)
#Out: Target at index: 5

