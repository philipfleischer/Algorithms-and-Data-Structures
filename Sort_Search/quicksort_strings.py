import sys
from file_to_list import make_list
from typing import List, TypeVar

T = TypeVar("T")

def quicksort(values: List[T]) -> List[T]:
    """Best case: O(n log(n)).
    Average is often best case: ( O(n log(n)))
    Worst case: O(n^2). """
    if len(values) <= 1:
        return values
    less_than_pivot: List[T] = []
    greater_than_pivot: List[T] = []
    pivot: T = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    

names: List[T] = make_list(sys.argv[1])
sorted_names = quicksort(names)
for n in sorted_names:
    print(n)



