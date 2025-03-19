import typer
from enum import Enum
from maze import load_maze
from visualization import MazeVisualizer
from benchmark import run_benchmark

from search_algorithms.random_search import RandomSearch
from search_algorithms.depth_first_search import DepthFirstSearch
from search_algorithms.breadth_first_search import BreadthFirstSearch
from search_algorithms.greedy_search import GreedySearch
from search_algorithms.a_star import AStarSearch

app = typer.Typer()


class Algorithm(str, Enum):
    RANDOM = "random"
    DFS = "dfs"
    BFS = "bfs"
    GREEDY = "greedy"
    ASTAR = "astar"


ALGORITHMS = {
    Algorithm.RANDOM: RandomSearch,
    Algorithm.DFS: DepthFirstSearch,
    Algorithm.BFS: BreadthFirstSearch,
    Algorithm.GREEDY: GreedySearch,
    Algorithm.ASTAR: AStarSearch,
}


@app.command()
def visualize(
    maze_path: str = typer.Argument(..., help="Path to the maze text file."),
    algorithm: Algorithm = typer.Argument(..., help="Algorithm to use."),
    step_by_step: bool = typer.Option(
        False, "--step-by-step", "-s", help="Show solving process step by step."
    ),
):
    """
    Load the maze, run the selected search algorithm, and display the results.
    """
    maze = load_maze(maze_path)
    search_algorithm = ALGORITHMS[algorithm]()
    result = search_algorithm.search(maze)
    visualizer = MazeVisualizer(maze)

    if step_by_step:
        visualizer.display_full_process(result.steps, result)
    else:
        visualizer.display_final_result(result)


@app.command()
def benchmark():
    """
    Run a benchmark comparing all search algorithms.
    """
    run_benchmark()


if __name__ == "__main__":
    app()
