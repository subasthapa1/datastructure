"""
This is a helper function to read maze, identify adjacent nodes, path and verify if
the maze is valid or not

"""

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def read_maze(filename):
    try:
        with open(filename, "r", newline=None) as fh:
            maze = [[char for char in line.strip("\r\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular")
                    raise SystemExit
                return maze

    except IOError:
        print("Invalid path. File not found")
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos
    num_cols = len(maze[0])
    num_rows = len(maze)
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path
