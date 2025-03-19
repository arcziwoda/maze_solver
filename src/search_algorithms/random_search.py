import random
from typing import override
from search_algorithms.search_algorithm import SearchAlgorithm, SearchResult, SearchStep
from maze import Maze


class RandomSearch(SearchAlgorithm):
    @override
    def search(self, maze: Maze) -> SearchResult:
        steps = []
        nodes_expanded = 0

        start = maze.start
        goal = maze.end

        frontier = [start]
        visited = set()
        parent = {}

        while frontier:
            current = random.choice(frontier)
            frontier.remove(current)
            nodes_expanded += 1
            visited.add(current)

            steps.append(
                SearchStep(current, list(frontier), set(visited), parent.copy())
            )

            if current == goal:
                path = self.reconstruct_path(parent, start, current)
                return SearchResult(path, nodes_expanded, steps)

            for neighbor in maze.get_neighbors(current):
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)
                    parent[neighbor] = current

        return SearchResult([], nodes_expanded, steps)
