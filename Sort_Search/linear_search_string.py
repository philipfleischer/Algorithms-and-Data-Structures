import sys
from file_to_list import make_list
from typing import List, TypeVar

T = TypeVar("T")

names: List[T] = make_list(sys.argv[1])
search_names: List[T] = make_list(sys.argv[2])

def index_of_item(collection, target):
    for i in range(0, len(collection)):
        if target == collection[i]:
            return i
    return None

for n in search_names:
    index = index_of_item(names, n)
    print(index)  