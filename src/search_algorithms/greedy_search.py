import heapq
from typing import override
from search_algorithms.search_algorithm import SearchAlgorithm, SearchResult, SearchStep
from maze import Maze


class GreedySearch(SearchAlgorithm):
    def heuristic(self, node, goal):
        """
        Compute the Manhattan distance between node and goal.
        """
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    @override
    def search(self, maze: Maze) -> SearchResult:
        steps = []
        nodes_expanded = 0

        frontier = []  # Priority queue: elements are tuples (f, counter, node)
        parent = {}
        counter = 0  # for ties

        start = maze.start
        goal = maze.end

        heapq.heappush(frontier, (self.heuristic(start, goal), counter, start))
        current_frontier_nodes = [start]  # for visualization
        counter += 1

        visited = set()

        while frontier:
            _, _, current = heapq.heappop(frontier)
            current_frontier_nodes.remove(current)
            if current in visited:
                continue

            visited.add(current)
            nodes_expanded += 1

            if current == goal:
                path = self.reconstruct_path(parent, start, current)
                return SearchResult(path, nodes_expanded, steps)

            for neighbor in maze.get_neighbors(current):
                if neighbor not in visited:
                    heapq.heappush(
                        frontier, (self.heuristic(neighbor, goal), counter, neighbor)
                    )
                    current_frontier_nodes.append(neighbor)
                    counter += 1
                    if neighbor not in parent:
                        parent[neighbor] = current

            steps.append(
                SearchStep(
                    current,
                    current_frontier_nodes.copy(),
                    visited.copy(),
                    parent.copy(),
                )
            )

        return SearchResult([], nodes_expanded, steps)
