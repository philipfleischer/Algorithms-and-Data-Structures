from typing import List, TypeVar

T = TypeVar("T")

def make_list(filename: str) -> List[T]:
    made_list: List[T] = []
    with open(filename, "r") as file:
        for line in file:
            made_list.append(line.strip())
    return made_list

