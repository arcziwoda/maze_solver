class Maze:
    def __init__(self, grid, start, end):
        """
        Initializes the Maze object.
        """
        self.grid = grid
        self.start = start
        self.end = end
        self.height = len(grid)
        self.width = len(grid[0]) if grid else 0

    def is_within_bounds(self, position):
        """
        Check if a given (x, y) position is within the maze bounds.
        """
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_wall(self, position):
        """
        Check if the given position is a wall.
        """
        x, y = position
        return self.grid[y][x] == "X"

    def get_neighbors(self, position):
        """
        Return accessible neighbors of the given position.
        Neighbors are the four adjacent cells (up, down, left, right)
        that are within bounds and not walls.
        """
        x, y = position
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (x + dx, y + dy)
            if self.is_within_bounds(new_pos) and not self.is_wall(new_pos):
                neighbors.append(new_pos)
        return neighbors

    def __str__(self):
        """
        Return a string representation of the maze.
        """
        return "\n".join("".join(row) for row in self.grid)


def load_maze(file_path):
    """
    Reads the maze from a text file and returns a Maze object.

    Expected file format:
      - A series of lines representing the maze grid.
      - Two additional lines at the end:
          start x, y
          end x, y
      where x and y are the coordinates.

    """
    with open(file_path, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    grid_lines = []
    start_line = None
    end_line = None

    for line in lines:
        lower_line = line.lower()
        if lower_line.startswith("start"):
            start_line = line
        elif lower_line.startswith("end"):
            end_line = line
        else:
            grid_lines.append(line)

    if start_line is None or end_line is None:
        raise ValueError("Maze file must include both start and end coordinates.")

    def parse_coordinate(line):
        """
        Parses a coordinate line of the form "start x, y" or "end x, y".
        Returns a tuple (x, y) as integers.
        """
        try:
            _, coord_part = line.split(maxsplit=1)
            x_str, y_str = coord_part.split(",")
            return int(x_str.strip()), int(y_str.strip())
        except Exception as e:
            raise ValueError(f"Invalid coordinate format in line: {line}") from e

    start = parse_coordinate(start_line)
    end = parse_coordinate(end_line)

    grid = [list(row) for row in grid_lines]

    return Maze(grid, start, end)
