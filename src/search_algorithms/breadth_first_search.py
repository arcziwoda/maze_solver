from typing import override
from search_algorithms.search_algorithm import SearchAlgorithm, SearchResult, SearchStep
from maze import Maze
from collections import deque


class BreadthFirstSearch(SearchAlgorithm):
    @override
    def search(self, maze: Maze, track_steps: bool = False) -> SearchResult:
        steps = []
        nodes_expanded = 0

        frontier = deque([maze.start])
        in_frontier = {maze.start}
        visited = set()
        parent = {}

        while frontier:
            current = frontier.popleft()
            in_frontier.discard(current)

            if current in visited:
                continue
            visited.add(current)
            nodes_expanded += 1

            if current == maze.end:
                path = self.reconstruct_path(parent, maze.start, current)
                return SearchResult(path, nodes_expanded, steps)

            for neighbor in maze.get_neighbors(current):
                if neighbor not in visited and neighbor not in in_frontier:
                    frontier.append(neighbor)
                    parent[neighbor] = current
            if track_steps:
                steps.append(
                    SearchStep(current, list(frontier), visited.copy(), parent.copy())
                )

        return SearchResult([], nodes_expanded, steps)
