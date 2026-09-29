# 8-Puzzle Solver using BFS and DFS

## Project Description

This project implements two uninformed search algorithms:

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)

Both algorithms are used to solve the **8-Puzzle problem**.

The 8-Puzzle consists of a 3 × 3 board containing numbers from 1 to 8 and one blank space. The objective is to move the tiles and reach the goal state.

## Goal State

```text
1 2 3
4 5 6
7 8 _
```

In the Python program, `0` represents the blank space.

## Problem Statement

Given an initial shuffled 8-puzzle configuration, find a sequence of moves that transforms the initial state into the goal state using BFS and DFS.

## Algorithms Used

### 1. Breadth-First Search (BFS)

BFS explores the state space level by level.

- Uses a Queue (FIFO).
- Explores states according to their depth.
- For equal-cost moves, BFS can find the shortest solution.
- It can require a large amount of memory.

### 2. Depth-First Search (DFS)

DFS explores one path as deeply as possible before backtracking.

- Uses a Stack (LIFO).
- Generally requires less frontier memory than BFS.
- Does not guarantee the shortest solution.
- Its performance depends on the search order.

## Input

The program currently uses this initial 8-puzzle state:

```text
1 2 3
5 _ 6
4 7 8
```

The same initial state is given to both algorithms so their performance can be compared.

To test another puzzle, change the `start` tuple in `bfs_dfs.py`.

## Output

The program displays:

- Initial state
- Solution path
- Solution length
- Number of nodes expanded
- Execution time in milliseconds

Example output format:

```text
Breadth-First Search (BFS)
Solution length: ... moves
Nodes expanded: ...
Execution time: ... ms

Depth-First Search (DFS)
Solution length: ... moves
Nodes expanded: ...
Execution time: ... ms
```

The exact values depend on the initial puzzle state and the computer on which the program is executed.

## Performance Measurement

Python's `time.perf_counter()` is used to measure execution time.

A node is counted as expanded when it is removed from the frontier and processed.

For a fair comparison, both algorithms use the same initial state.

## Comparison

| Feature | BFS | DFS |
|---|---|---|
| Search Type | Uninformed | Uninformed |
| Data Structure | Queue | Stack |
| Search Strategy | Level by level | Deep first |
| Complete | Yes for finite reachable state space | Depends on implementation/search space |
| Shortest Solution | Yes, for equal-cost moves | No |
| Memory | Higher | Generally lower |
| 8-Puzzle Use | Suitable for finding shortest paths | Useful for demonstrating depth-first exploration |

## Project Structure

```text
8-Puzzle-BFS-DFS/
│
├── bfs_dfs.py
└── README.md
```

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to Run

Open the project folder in VS Code.

Open the terminal and run:

```bash
python bfs_dfs.py
```

On some systems, use:

```bash
python3 bfs_dfs.py
```

## Expected Result

The program runs BFS and DFS on the same 8-puzzle state and reports their solution length, nodes expanded, and execution time.

BFS is expected to find a shortest solution for equal-cost puzzle moves. DFS may find a different, non-shortest solution depending on the order in which states are explored.

## Conclusion

This project demonstrates the difference between BFS and DFS for solving the 8-puzzle problem. BFS searches systematically level by level and can guarantee the shortest solution for equal-cost moves. DFS explores deeply before backtracking and does not guarantee the shortest solution.

Profiling the two algorithms using execution time, nodes expanded, and solution length provides a practical way to compare their search behavior.
