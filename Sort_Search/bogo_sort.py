import random
import sys
from Sort_Search.file_to_list import make_list

def is_sorted(values: list[int]) -> bool:
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True


def bogo_sort(values: list[int]) -> bool:
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values

numbers = make_list(sys.argv[1])
print(bogo_sort(numbers))
