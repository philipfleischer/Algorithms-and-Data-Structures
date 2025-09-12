from typing import List, TypeVar

T = TypeVar("T")

def merge_sort(arr: List[T]) -> List[T]:
    """Sorts a list in ascending order.
    Returns a new sorted list.

    Divide: Find the midpoint of the list and divide into sublists.
    Conquer: Recursively sort the sublists created in previous step.
    Combine: Merge the sorted sublists creted in previous step. 
    
    Takes O(n*log(n)) time. """

    if len(arr) <= 1:
        return arr
    
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(arr: List[T]) -> List[T]:
    """Divide the unsorted list at midpoint into sublists.
    Returns two sublists - left and right. 
    Takes overall O(log(n)) time. """

    mid = len(arr) // 2
    
    #TODO: Use Binary Search here to not have O(k*n*log(n)) time
    left = arr[:mid]    #Does not include mid
    right = arr[mid:]   #Includes mid

    return left, right


def merge(left_arr: List[T], right_arr: List[T]) -> List[T]:
    """Merges two lists (arrays), sorting them in the process.
    Returns a new merged list.
    Runs in overall O(n) time. """

    array = []
    index_left_arr = 0
    index_right_arr = 0

    while index_left_arr < len(left_arr) and index_right_arr < len(right_arr):
        if left_arr[index_left_arr] < right_arr[index_right_arr]:
            array.append(left_arr[index_left_arr])
            index_left_arr += 1
        else:
            array.append(right_arr[index_right_arr])
            index_right_arr += 1
        
    while index_left_arr < len(left_arr):
        array.append(left_arr[index_left_arr])
        index_left_arr += 1

    while index_right_arr < len(right_arr):
        array.append(right_arr[index_right_arr])
        index_right_arr += 1
    return array


def verify_sorted(array):
    arr_length = len(array)

    if arr_length == 0 or arr_length == 1:
        return True
    
    return array[0] < array[1] and verify_sorted(array[1:])

alist = [52, 62, 93, 17, 77, 31, 44, 55, 20]
arr = merge_sort(alist)
print(arr)
print(verify_sorted(alist))
print(verify_sorted(arr))
    
    