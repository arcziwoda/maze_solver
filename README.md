# Maze Solver

## Introduction

This project implements **five systematic state space search algorithms** to solve mazes. The program allows users to **visualize** the search process and **benchmark** the algorithms' performance.

## Features

- **Maze solving using five search algorithms:**
  - Random Search
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Greedy Search
  - A\* Search (Guaranteed optimal path)
- **Visualization of algorithm execution**
- **Benchmarking against optimal path lengths**

## Installation

1. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Visualizing a Maze Solution

To solve a maze using a specific algorithm and visualize the process, run:

```bash
python src/main.py visualize <maze_path> <algorithm>
```

#### Parameters

- `<maze_path>`: Path to the maze text file.
- `<algorithm>`: Algorithm to use (`random`, `dfs`, `bfs`, `greedy`, `astar`).
- `--step-by-step` (`-s`): Optional flag to enable step-by-step visualization.

#### Example

```bash
python src/main.py visualize data/test/26.txt bfs --step-by-step
```

### Running Benchmarks

To compare the efficiency of all algorithms against optimal path lengths:

```bash
python src/main.py benchmark
```

This command will:

- Solve all test mazes.
- Compare found paths to optimal paths.
- Display time taken for each algorithm.

## Search Algorithms

- **Random Search**: Randomly explores paths until it finds a solution.
- **Depth-First Search (DFS)**: Explores as deep as possible before backtracking.
- **Breadth-First Search (BFS)**: Explores all nodes at the current depth before moving deeper (guarantees shortest path in uniform cost mazes).
- **Greedy Search**: Expands nodes based only on the shortest heuristic distance to the goal.
- **A\* Search**: Uses a heuristic along with a path cost to always find optimal path.

## Maze Format

Mazes are stored as text files with the following format:

```
XXXXXXXXXXXXX
X           X
X  XXXXXXX  X
X     X     X
X X X X XXX X
X X         X
XX  X XXXXX X
X   X       X
X X X XXX XXX
X           X
X XXX X   X X
X           X
XXXXXXXXXXXXX
start 1, 7
end 5, 3
```

- `X` represents walls.
- Spaces represent open paths.
- The `start` and `end` positions are given in Cartesian coordinates (top-left origin, y-axis positive downward).
