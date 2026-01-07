# Algorithms-and-Data-Structures

## IN2010 – Algorithms and Data Structures (UiO)

This repository contains my coursework for **IN2010 – Algorithms and Data Structures** at the University of Oslo (UiO).
It includes **five graded submissions (Innlevering 1–5)** and a **Notes** folder with supporting material (summaries, explanations, and references used during the course).

All projects are preserved with complete Git history from the original UiO repositories.

| Project       | Description                                                                 | Browse                                                                            | Commit History                                                                             |
| ------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Innlevering 1 | Teque (triple-ended queue): push_front/back/middle + get with efficient ops | [Files](https://github.com/philipfleischer/Algorithms-and-Data-Structures/oblig1) | [Commits](https://github.com/philipfleischer/Algorithms-and-Data-Structures/commits/main/) |
| Innlevering 2 | Efficient Sets using BST + AVL, plus building balanced BST insertion order  | [Files](https://github.com/philipfleischer/Algorithms-and-Data-Structures/oblig2) | [Commits](https://github.com/philipfleischer/Algorithms-and-Data-Structures/commits/main/) |
| Innlevering 3 | Kattunge (tree path to root) + sorting algorithms + performance metrics     | [Files](https://github.com/philipfleischer/Algorithms-and-Data-Structures/oblig3) | [Commits](https://github.com/philipfleischer/Algorithms-and-Data-Structures/commits/main/) |
| Innlevering 4 | IMDB graph: build large graph, shortest paths, weighted “chill” paths, CCs  | [Files](https://github.com/philipfleischer/Algorithms-and-Data-Structures/oblig4) | [Commits](https://github.com/philipfleischer/Algorithms-and-Data-Structures/commits/main/) |
| Innlevering 5 | Mandatory submission: analysis + balanced BST + sorting + IMDB graph tasks  | [Files](https://github.com/philipfleischer/Algorithms-and-Data-Structures/oblig1) | [Commits](https://github.com/philipfleischer/Algorithms-and-Data-Structures/commits/main/) |
| Notes         | Course notes: key concepts, summaries, and quick references                 | [Files](https://github.com/philipfleischer/Algorithms-and-Data-Structures/Notes)  | [Commits](https://github.com/philipfleischer/Algorithms-and-Data-Structures/commits/main/) |

⸻

## Course focus

The course covers fundamental data structures and algorithms with emphasis on:

- Time and space complexity analysis (Big-O)
- Abstract data types and correct interface design
- Trees: BSTs, AVL trees, balancing strategies
- Queues, deques, and specialized variants (e.g. teque)
- Sorting algorithms and empirical performance analysis
- Graph representations and algorithms (BFS, shortest paths, connected components)
- Practical algorithm engineering on large datasets

All solutions are implemented with correctness, efficiency, and clarity as primary goals.

⸻

## Techniques and algorithms used

Across the submissions, the following techniques and algorithms are implemented and analyzed:

- Queue variants using split structures for O(1) operations
- Binary Search Trees and AVL Trees
- Recursive and iterative tree algorithms
- Insertion sort, merge sort, and additional comparison-based sorting algorithms
- Instrumentation of algorithms to count comparisons, swaps, and execution time
- Breadth-first search (BFS) for shortest paths in unweighted graphs
- Dijkstra’s algorithm for weighted shortest paths
- Graph traversal for connected component analysis

⸻

## Graph processing at scale

One of the central parts of the course involves building and analyzing a **large real-world graph**
based on IMDB data:

- ~100,000 nodes (actors)
- ~5 million edges (shared movie appearances)
- Multiple graph representations explored
- Efficient traversal and shortest-path computation
- Weighted pathfinding using custom cost functions

This provides hands-on experience with performance constraints that do not appear in small toy examples.

⸻

## Repository structure

IN2010-Algorithms-and-Data-Structures/
├── oblig1/ # Teque and complexity analysis
├── oblig2/ # Sets with BST/AVL and balanced tree construction
├── oblig3/ # Tree traversal + sorting and performance measurement
├── oblig4/ # Large-scale IMDB graph algorithms
├── oblig5/ # Mandatory combined submission
└── Notes/ # Course notes, summaries, and references

⸻

## Notes

The `Notes/` directory contains personal summaries and explanations used during the course.
These are intended as **learning material and quick reference**, not polished lecture notes.

⸻

## Language and environment

- Primary language: **Python** (some assignments optionally in Java)
- Standard libraries only, unless explicitly allowed
- All programs are designed to be run from the command line
- Input/output strictly follows the formats specified in each assignment

⸻

## Academic context

This repository represents coursework completed as part of the
**IN2010 – Algorithms and Data Structures** course at the University of Oslo.

All implementations are my own and written for educational purposes.
