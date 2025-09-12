import sys
from pathlib import Path
import heapq

def balanced_print_tree_pq(arr: list[int]) -> None:
    heap: list[tuple[int, int, int]] = []
    seqNum = 0

    def _heap_push(low: int, high: int) -> None:
        nonlocal seqNum
        if low <= high:
            seqNum += 1
            heapq.heappush(heap, (-seqNum, low, high))
    
    _heap_push(0, len(arr) - 1)

    while heap:
        _, low, high = heapq.heappop(heap)
        mid = (low + high + 1) // 2
        print(arr[mid])
        _heap_push(low, mid-1)
        _heap_push(mid + 1, high)


def _read_file_to_list(filename: str) -> heapq:
    sorted_array: list[int] = []
    with open(filename, "r") as f:
        for line in f:
            line_strip = line.strip()
            sorted_array.append(int(line_strip))
    return sorted_array


def main():
    base = Path(__file__).parent
    arg = sys.argv[1]
    path = Path(arg)
    if not path.is_absolute():
        path = base / path
    
    sorted_array = _read_file_to_list(str(path))
    #sorted_array = [0,1,2,3,4,5,6,7,8,9,10]
    balanced_print_tree_pq(sorted_array)

if __name__ == "__main__":
    main()