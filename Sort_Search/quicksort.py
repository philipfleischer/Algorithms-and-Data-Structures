import sys
from Sort_Search.file_to_list import make_list
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
    #print("%15s %ls %-15s" % (less_than_pivot, pivot, greater_than_pivot)) 
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
    
numbers: List[T] = make_list(sys.argv[1])
#numbers: List[T] = [4,6,3,2,9,7,3,5]
#print(quicksort(numbers))
quicksort(numbers)

"""
python quicksort_strings.py Tester/names.txt Tester/names_small.txt > names/sorted.txt
"""
