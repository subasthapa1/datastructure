
def read_maze(filename):
    try:
        with open(filename) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze

    except OSError:
        print("Filename not found. Please check the filename provided.")

if __name__ == "__main__":
    maze = read_maze("mazes/modest_maze.txt")
    for row in maze:
        print(row)
    print("--------------------------")
    maze = read_maze("mazes/challenge_maze.txt")
    for row in maze:
        print(row)
