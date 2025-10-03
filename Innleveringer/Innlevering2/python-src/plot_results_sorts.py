#!/usr/bin/env python3
# plot_results_sorts.py
#
# Usage:
#   python3 plot_results_sorts.py path/to/<stem>_results.csv
#
# Outputs (in output/plots/):
#   - all_time.png, all_compares.png, all_swaps.png
#   - <alg>_time.png, <alg>_compares.png, <alg>_swaps.png
#   - metadata.txt

import sys
import os
import csv
import time
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt

# --------------- IO helpers ---------------


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def stem_of(csv_path: str) -> str:
    base = os.path.basename(csv_path)
    if base.endswith(".csv"):
        base = base[:-4]
    return base


# --------------- Parse CSV ---------------


def parse_results_csv(
    csv_path: str,
) -> Tuple[List[int], Dict[str, Dict[str, List[int]]]]:
    """
    Returns:
      n_values: list[int]
      data: dict[alg][metric] -> list[int], where metric in {"cmp","swaps","time"}
    The CSV header is expected to look like:
      n, <alg>_cmp, <alg>_swaps, <alg>_time, <alg2>_cmp, ...
    """
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        # Normalize header tokens (strip spaces)
        header = [h.strip() for h in header]

        # Identify metric columns
        if len(header) == 0 or header[0].lower() != "n":
            raise ValueError("First column must be 'n'")

        # Map: alg -> metric -> column index
        alg_cols: Dict[str, Dict[str, int]] = {}
        for idx, name in enumerate(header[1:], start=1):
            parts = name.split("_")
            if len(parts) < 2:
                # ignore unknown columns
                continue
            alg = "_".join(parts[:-1]).lower()
            metric = parts[-1].lower()
            if metric not in {"cmp", "swaps", "time"}:
                continue
            alg_cols.setdefault(alg, {})[metric] = idx

        # Prepare containers
        n_values: List[int] = []
        data: Dict[str, Dict[str, List[int]]] = {
            alg: {"cmp": [], "swaps": [], "time": []} for alg in alg_cols.keys()
        }

        # Read rows
        for row in reader:
            if not row:
                continue
            n = int(row[0].strip())
            n_values.append(n)
            for alg, cols in alg_cols.items():
                for metric in ("cmp", "swaps", "time"):
                    col = cols.get(metric, None)
                    if col is None or col >= len(row):
                        # Missing column for this metric; treat as 0
                        val = 0
                    else:
                        # Allow empty/space entries
                        cell = row[col].strip()
                        val = int(cell) if cell else 0
                    data[alg][metric].append(val)

        return n_values, data


# --------------- Plotting ---------------


def plot_all(n_values: List[int], data: Dict[str, Dict[str, List[int]]], outdir: str):
    """One figure per metric with all algorithms overlayed."""
    ensure_dir(outdir)

    # (1) Time
    plt.figure()
    for alg, series in data.items():
        plt.plot(n_values, series["time"], label=alg)
    plt.xlabel("n")
    plt.ylabel("time (µs)")
    plt.title("n vs time (all algorithms)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "all_time.png"))
    plt.close()

    # (2) Comparisons
    plt.figure()
    for alg, series in data.items():
        plt.plot(n_values, series["cmp"], label=alg)
    plt.xlabel("n")
    plt.ylabel("comparisons")
    plt.title("n vs comparisons (all algorithms)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "all_compares.png"))
    plt.close()

    # (3) Swaps/moves
    plt.figure()
    for alg, series in data.items():
        plt.plot(n_values, series["swaps"], label=alg)
    plt.xlabel("n")
    plt.ylabel("swaps/moves")
    plt.title("n vs swaps/moves (all algorithms)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(outdir, "all_swaps.png"))
    plt.close()


def plot_per_alg(
    n_values: List[int], data: Dict[str, Dict[str, List[int]]], outdir: str
):
    """Three figures per algorithm: time, comparisons, swaps."""
    ensure_dir(outdir)
    for alg, series in data.items():
        # Time
        plt.figure()
        plt.plot(n_values, series["time"])
        plt.xlabel("n")
        plt.ylabel("time (µs)")
        plt.title(f"{alg}: n vs time")
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, f"{alg}_time.png"))
        plt.close()

        # Comparisons
        plt.figure()
        plt.plot(n_values, series["cmp"])
        plt.xlabel("n")
        plt.ylabel("comparisons")
        plt.title(f"{alg}: n vs comparisons")
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, f"{alg}_compares.png"))
        plt.close()

        # Swaps/moves
        plt.figure()
        plt.plot(n_values, series["swaps"])
        plt.xlabel("n")
        plt.ylabel("swaps/moves")
        plt.title(f"{alg}: n vs swaps/moves")
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, f"{alg}_swaps.png"))
        plt.close()


# --------------- Main ---------------


def main():
    if len(sys.argv) != 2:
        print(
            f"Usage: {os.path.basename(sys.argv[0])} path/to/<stem>_results.csv",
            file=sys.stderr,
        )
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.isfile(csv_path):
        print(f"Not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    # Parse data
    n_values, data = parse_results_csv(csv_path)

    # Output dirs
    root_out = os.path.join("output", "plots")
    ensure_dir(root_out)

    # Plots
    plot_all(n_values, data, root_out)
    plot_per_alg(n_values, data, root_out)

    # Metadata
    write_metadata(n_values, data, csv_path, root_out)

    print(f"Figures written to: {root_out}")
    print(
        "Created: all_time.png, all_compares.png, all_swaps.png, and per-algorithm figures."
    )


if __name__ == "__main__":
    main()
