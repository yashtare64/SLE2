from collections import deque
import time

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def get_neighbors(state):
    """Generate all valid next states."""
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[new_blank] = (
                new_state[new_blank],
                new_state[blank],
            )
            neighbors.append(tuple(new_state))

    return neighbors


def reconstruct_path(parent, state):
    """Reconstruct the solution path from start to goal."""
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()
    return path


def bfs(start):
    """Breadth-First Search for the 8-puzzle."""
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL:
            return reconstruct_path(parent, current), nodes_expanded

        for next_state in get_neighbors(current):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)

    return None, nodes_expanded


def dfs(start):
    """Depth-First Search for the 8-puzzle."""
    stack = [start]
    visited = {start}
    parent = {start: None}
    nodes_expanded = 0

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current == GOAL:
            return reconstruct_path(parent, current), nodes_expanded

        # Reverse order keeps the search order consistent with BFS neighbors.
        for next_state in reversed(get_neighbors(current)):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                stack.append(next_state)

    return None, nodes_expanded


def print_state(state):
    """Print one 8-puzzle state."""
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i + 3]))
    print()


def run_algorithm(name, algorithm, start):
    """Run an algorithm and display profiling results."""
    start_time = time.perf_counter()
    path, nodes_expanded = algorithm(start)
    end_time = time.perf_counter()

    elapsed_ms = (end_time - start_time) * 1000

    print("=" * 50)
    print(name)
    print("=" * 50)

    if path is None:
        print("No solution found.")
    else:
        print("Solution path:")
        for step, state in enumerate(path):
            print(f"Step {step}:")
            print_state(state)

        print(f"Solution length: {len(path) - 1} moves")

    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Execution time: {elapsed_ms:.4f} ms")
    print()


def main():
    # Same start state can be used for both algorithms for fair comparison.
    start = (
        1, 2, 3,
        5, 0, 6,
        4, 7, 8
    )

    print("8-PUZZLE SOLVER: BFS vs DFS")
    print("=" * 50)
    print("Initial State:")
    print_state(start)

    run_algorithm("Breadth-First Search (BFS)", bfs, start)
    run_algorithm("Depth-First Search (DFS)", dfs, start)


if __name__ == "__main__":
    main()
