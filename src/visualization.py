import os
import time
from colorama import Back, Style, init
from search_algorithms.search_algorithm import SearchResult, SearchStep

init(autoreset=True)


def clear():
    """
    Clears the terminal screen in a platform-independent way.
    """
    os.system("cls" if os.name == "nt" else "clear")


class MazeVisualizer:
    def __init__(self, maze):
        self.maze = maze

    def print_legend(self):
        """
        Prints a color legend to explain the visual elements.
        """
        print("\nLegend:")
        print(Back.GREEN + " S " + Style.RESET_ALL + " - Start")
        print(Back.RED + " E " + Style.RESET_ALL + " - End")
        print(Back.BLUE + "   " + Style.RESET_ALL + " - Opened (visited) node")
        print(Back.MAGENTA + "   " + Style.RESET_ALL + " - Final path")
        print(Back.WHITE + "   " + Style.RESET_ALL + " - Wall")

    def display(
        self,
        current_step: SearchStep | None = None,
        final_path: list[tuple[int, int]] | None = None,
        opened_nodes: set[tuple[int, int]] | None = None,
    ):
        """
        Display the maze with colored output.
        """
        grid = [row.copy() for row in self.maze.grid]

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "X":
                    grid[y][x] = Back.WHITE + " " + Style.RESET_ALL

        sx, sy = self.maze.start
        ex, ey = self.maze.end
        grid[sy][sx] = Back.GREEN + "S" + Style.RESET_ALL
        grid[ey][ex] = Back.RED + "E" + Style.RESET_ALL

        if current_step:
            for vx, vy in current_step.visited:
                if (vx, vy) not in (self.maze.start, self.maze.end):
                    grid[vy][vx] = Back.BLUE + " " + Style.RESET_ALL
            for fx, fy in current_step.frontier:
                if (fx, fy) not in (self.maze.start, self.maze.end):
                    grid[fy][fx] = Back.YELLOW + " " + Style.RESET_ALL

        if final_path:
            for px, py in final_path:
                if (px, py) not in (self.maze.start, self.maze.end):
                    grid[py][px] = Back.MAGENTA + " " + Style.RESET_ALL

        if opened_nodes:
            for ox, oy in opened_nodes:
                if (ox, oy) not in (self.maze.start, self.maze.end) and grid[oy][
                    ox
                ] == self.maze.grid[oy][ox]:
                    grid[oy][ox] = Back.BLUE + " " + Style.RESET_ALL

        for row in grid:
            print("".join(row))

        if final_path is not None:
            self.print_legend()

    def display_final_result(self, final_result: SearchResult):
        """
        Display final result (final path, opened nodes, legend).
        """
        opened_nodes = final_result.steps[-1].visited if final_result.steps else None
        self.display(final_path=final_result.path, opened_nodes=opened_nodes)
        print(f"Nodes expanded: {final_result.nodes_expanded}")
        if final_result.path:
            print(f"Path length: {len(final_result.path) - 1}")
        else:
            print("No path found.")

    def display_full_process(self, steps: list[SearchStep], final_result: SearchResult):
        """
        Animate the search process, then display the final result with both the correct path and all opened nodes.
        """
        for step in steps:
            clear()
            self.display(current_step=step)
            time.sleep(0.1)
        clear()
        self.display_final_result(final_result)
