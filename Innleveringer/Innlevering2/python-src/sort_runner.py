#!/usr/bin/env python3
from countcompares import CountCompares
from countswaps import CountSwaps
import insertion
import quick
import merge
import heapsort
import math
import time
import os

# ------------------- Configuration -------------------

# Algorithms for part 1 (write sorted .out files)
ALGS1 = [insertion.sort, quick.sort, merge.sort, heapsort.heapsort]
# Algorithms for part 2 (CSV with prefix runs)
ALGS2 = [insertion.sort, quick.sort, merge.sort, heapsort.heapsort]

# Time limit for a single sorting (per prefix run) in milliseconds
TIME_LIMIT_MS = 100
# Increment of n for prefix growth in part 2
INCREMENT = 1

# Output directory for all generated files
OUTPUT_DIR = "output"


# ------------------- Helpers -------------------


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def stem_of(filename: str) -> str:
    """Return filename without directories and extension."""
    return os.path.splitext(os.path.basename(filename))[0]


def out_path(stem: str, suffix: str) -> str:
    """Build an output path inside OUTPUT_DIR for this stem and suffix."""
    ensure_output_dir()
    return os.path.join(OUTPUT_DIR, f"{stem}{suffix}")


def algname(alg):
    """Use the module name (lowercase) as algorithm label."""
    return alg.__module__.lower()


# ------------------- Part 1: write sorted outputs -------------------


def run_algs_part1(A, infilename):
    s = stem_of(infilename)
    for alg in ALGS1:
        # Wrap data for counting
        countA = CountSwaps([CountCompares(x) for x in A])
        # Run algorithm; assume it returns an iterable of sorted elements
        sorted_out = alg(countA)
        # If the algorithm sorts in-place and returns None, fall back to the wrapped list
        if sorted_out is None:
            sorted_out = countA
        # Convert CountCompares -> plain ints when writing
        out_lines = (
            str(x.elem if isinstance(x, CountCompares) else x) for x in sorted_out
        )
        outfilename = out_path(s, f"_{algname(alg)}.out")
        with open(outfilename, "w", encoding="utf-8") as f:
            f.write("\n".join(out_lines))


# ------------------- CSV header & formatting -------------------


def algheader(alg):
    name = algname(alg)
    return f"{name}_cmp, {name}_swaps, {name}_time"


def makeheader(algs, digits):
    headers = ", ".join(algheader(a) for a in algs)
    fmt = f"%{digits}s, %s"
    return fmt % ("n", headers)


def runstringfmt(alg):
    c, s, t = map(len, algheader(alg).split(", "))
    fmt = f"%{c}d, %{s}d, %{t}d"
    return fmt


# ------------------- Measure one algorithm on prefix i -------------------


def runalg(alg, A, i, discarded):
    fmt = runstringfmt(alg)

    if alg in discarded:
        res = fmt % (0, 0, 0)
        return res.replace("0", " ")

    # Wrap only the prefix
    countingA = CountSwaps([CountCompares(x) for x in A[:i]])

    start = time.time()
    alg(countingA)
    timeus = (time.time() - start) * 1_000_000
    timems = timeus / 1000.0

    if timems > TIME_LIMIT_MS:
        discarded.add(alg)
        print("\nGiving up on " + algname(alg) + "\n")

    comparisons = sum(x.compares for x in countingA)
    swaps = countingA.swaps

    return fmt % (comparisons, swaps, timeus)


# ------------------- Part 2: CSV with prefix runs -------------------


def run_algs_part2(A, infilename):
    s = stem_of(infilename)
    outfilename = out_path(s, "_results.csv")
    discarded = set()

    with open(outfilename, "w", encoding="utf-8") as f:
        digits = int(math.log10(len(A)) + 1) if len(A) > 0 else 1
        header = makeheader(ALGS2, digits)
        f.write(header + "\n")
        print(header)

        rowfmt = f"%{digits}d"
        last_print = time.time_ns()

        for i in range(0, len(A) + 1, INCREMENT):
            row = rowfmt % i

            for alg in ALGS2:
                row += ", " + runalg(alg, A, i, discarded)

            if set(ALGS2) == discarded:
                break

            f.write(row + "\n")

            now = time.time_ns()
            if now - last_print > 1_000_000_000:  # ~1s
                print(row)
                last_print = now
                f.flush()


# ------------------- Entry points (call these from your driver) -------------------


def run_all(A, infilename):
    """Convenience: run part1 (.out files) and part2 (results.csv)."""
    run_algs_part1(A, infilename)
    run_algs_part2(A, infilename)
