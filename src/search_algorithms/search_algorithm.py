from abc import ABC, abstractmethod
from maze import Maze


class SearchStep:
    def __init__(self, current_node, frontier, visited, parent):
        """
        :param current_node: The node that was expanded in this step.
        :param frontier: The list of nodes queued for expansion.
        :param visited: The set of nodes already expanded.
        :param parent: A snapshot of the parent mapping used to reconstruct the path.
        """
        self.current_node = current_node
        self.frontier = frontier
        self.visited = visited
        self.parent = parent


class SearchResult:
    def __init__(
        self, path: list[tuple[int]], nodes_expanded: int, steps: list[SearchStep]
    ):
        """
        :param path: List of coordinates from start to end if a solution is found,
                     or None if not.
        :param nodes_expanded: Total number of nodes expanded during the search.
        :param steps: A list of SearchStep instances capturing the search process.
        """
        self.path = path
        self.nodes_expanded = nodes_expanded
        self.steps = steps


class SearchAlgorithm(ABC):
    @abstractmethod
    def search(self, maze: Maze) -> SearchResult:
        """
        Executes the search on the given maze.
        """
        pass

    def reconstruct_path(self, parent, start, goal):
        """
        Reconstructs the path from start to goal using the parent mapping.
        """
        path = []
        current = goal
        while current in parent:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()
        return path
