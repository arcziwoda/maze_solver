import os
import time
import colorama
from colorama import Fore, Style
from maze import load_maze
from search_algorithms.a_star import AStarSearch
from search_algorithms.breadth_first_search import BreadthFirstSearch
from search_algorithms.depth_first_search import DepthFirstSearch
from search_algorithms.greedy_search import GreedySearch
from search_algorithms.random_search import RandomSearch

colorama.init(autoreset=True)

ALGORITHMS = {
    "A*": AStarSearch(),
    "BFS": BreadthFirstSearch(),
    "DFS": DepthFirstSearch(),
    "Greedy": GreedySearch(),
    "Random": RandomSearch(),
}

TEST_FOLDER = "data/test"


def get_optimal_path_length(filename):
    """Extracts the optimal path length from the filename (e.g., '15.txt' -> 15)."""
    return int(os.path.splitext(filename)[0])


def run_benchmark():
    print(f"\n{Style.BRIGHT}Benchmarking Search Algorithms:\n")

    for file in sorted(
        os.listdir(TEST_FOLDER),
        key=lambda filename: int(get_optimal_path_length(filename)),
    ):
        optimal_length = get_optimal_path_length(file)
        maze_path = os.path.join(TEST_FOLDER, file)
        maze = load_maze(maze_path)

        print(
            f"{Style.BRIGHT}Maze: {file} (Optimal Path: {optimal_length}){Style.RESET_ALL}"
        )

        for name, algorithm in ALGORITHMS.items():
            start_time = time.time()
            result = algorithm.search(maze)
            elapsed_time = time.time() - start_time

            found_length = len(result.path) - 1 if result.path else float("inf")

            if found_length == optimal_length:
                color = Fore.GREEN
            elif found_length > optimal_length:
                color = Fore.YELLOW
            else:
                color = Fore.RED

            print(
                f"  {color}{name}: Found {found_length}, Time: {elapsed_time:.6f}s{Style.RESET_ALL}"
            )

        print("".rjust(40, "-"))
