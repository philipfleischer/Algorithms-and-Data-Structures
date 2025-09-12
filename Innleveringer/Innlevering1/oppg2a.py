import sys
from pathlib import Path

def balanced_print_tree(arr: list[int]) -> list[int]:
    def _print_midpoint(low: int, high: int) -> None:
        if low > high: return
        mid = (low + high +1 ) // 2
    
        print(arr[mid])
        _print_midpoint(mid+1, high)
        _print_midpoint(low, mid-1)
    
    _print_midpoint(0, len(arr) - 1)

def _read_file_to_list(filename: str) -> list[int]:
    with open(filename, "r") as f:
        sorted_array: list[int] = []
        for line in f:
            sorted_array.append(line)
        return sorted_array


def main():
    base = Path(__file__).parent
    arg = sys.argv[1]
    path = Path(arg)
    if not path.is_absolute():
        path = base / path

    #sorted_array = [0,1,2,3,4,5,6,7,8,9,10]
    sorted_array = _read_file_to_list(str(path))
    balanced_print_tree(sorted_array)

if __name__ == "__main__":
    main()