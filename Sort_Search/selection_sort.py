import sys
from Sort_Search.file_to_list import make_list

def selection_sort(values: list[int]) -> list[int]:
    """Time complexity: O(n^2)"""
    sorted_list = []
    #print("%-25s %-25s" % (values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        #print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index


numbers = make_list(sys.argv[1])
#print(selection_sort(numbers)) 
selection_sort(numbers)
    