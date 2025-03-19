import heapq
from typing import override
from search_algorithms.search_algorithm import SearchAlgorithm, SearchResult, SearchStep
from maze import Maze


class AStarSearch(SearchAlgorithm):
    def heuristic(self, node: tuple[int, int], goal: tuple[int, int]):
        """
        Compute the Manhattan distance between node and goal.
        """
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    @override
    def search(self, maze: Maze, track_steps: bool = False) -> SearchResult:
        steps = []
        nodes_expanded = 0

        frontier = []  # Priority queue: elements are tuples (f, counter, node)
        costs = {}
        parent = {}
        counter = 0  # for ties

        current_frontier_nodes = []  # for visualisation

        start = maze.start
        goal = maze.end

        costs[start] = 0
        heapq.heappush(frontier, (self.heuristic(start, goal), counter, start))
        current_frontier_nodes.append(start)
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
                potential_new_cost = costs[current] + 1
                if neighbor not in costs or potential_new_cost < costs[neighbor]:
                    costs[neighbor] = potential_new_cost
                    parent[neighbor] = current
                    f = potential_new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(frontier, (f, counter, neighbor))
                    current_frontier_nodes.append(neighbor)
                    counter += 1

            if track_steps:
                steps.append(
                    SearchStep(
                        current,
                        current_frontier_nodes.copy(),
                        visited.copy(),
                        parent.copy(),
                    )
                )

        return SearchResult([], nodes_expanded, steps)
