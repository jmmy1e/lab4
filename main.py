"""
LAB #4
    09/15/2025
    Student 1: Jimmy Le
    Student 2: Daniel McCray

    File IO: Create a program that allows the user to solve a maze that is read in from a file. The user will 
    begin at the starting point (‘s’) of the maze and will be able to move up, down, left, or right to 
    move through the maze. When the user reaches the finish (‘f’), they have solved the maze
"""

import check_input

def read_maze(file_name):
    """
    Read a maze file into a 2D list of characters.
    Only the trailing newline is removed so spaces inside rows are preserved.
    """
    maze = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            # Keep spaces intact
            row = list(line.rstrip('\n'))
            if row:  # Ignore completely empty lines
                maze.append(row)

    if not maze:
        raise ValueError('Maze file is empty.')

    # Verify the maze is rectangular and all rows are the same length
    width = len(maze[0])
    for r in maze:
        if len(r) != width:
            raise ValueError('All rows in the maze must be the same length.')

    return maze


def find_start(maze):
    """
    Find the starting position 's' in the maze.
    """
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 's':
                return [i, j]  # returns a list
    return None


def display_maze(maze, loc):
    """
    Display the maze with the current location marked with 'X'.
    """
    pr, pc = loc
    for r, row in enumerate(maze):
        line = []
        for c, ch in enumerate(row):
            if r == pr and c == pc:
                line.append('X')
            else:
                line.append(ch)
        print(''.join(line))
    print()  # blank line for readability


def main():
    """
    Loads the maze from 'maze.txt'
    Checks for start 's' and at least one finish 'f'
    Prompts the user to move until they reach 'f'
    """
    file_name = "maze.txt"
    try:
        maze = read_maze(file_name)
    except FileNotFoundError:
        print(f'Could not open "{file_name}". Make sure it is in the same folder as this program.')
        return
    except ValueError as e:
        print(f'Maze error: {e}')
        return

    start = find_start(maze)
    if start is None:
        print("Maze is missing a start cell 's'.")
        return

    # Ensure there is at least one finish 'f' somewhere in the maze
    has_finish = any('f' in row for row in maze)
    if not has_finish:
        print("Maze is missing a finish cell 'f'.")
        return

    # Current location as a list [row, col] to allow in-place updates
    loc = [start[0], start[1]]

    print("Welcome to the Maze Game!")
    display_maze(maze, (loc[0], loc[1]))

    while True:
        # Win check at the start of each loop
        if maze[loc[0]][loc[1]] == 'f':
            print("Congratulations, you solved the maze!")
            break

        # Prompt user: integers 1–4 only (validated by check_input module)
        choice = check_input.get_int_range(
            "1. Go North\n2. Go South\n3. Go East\n4. Go West\nEnter choice: ",
            1, 4
        )

        # Normalize numeric choices to letter directions
        mapping = {1: 'n', 2: 's', 3: 'e', 4: 'w'}
        move = mapping[choice]

        # Translate direction to row/col deltas
        dr, dc = 0, 0
        if move == 'n':
            dr = -1
        elif move == 's':
            dr = 1
        elif move == 'e':
            dc = 1
        elif move == 'w':
            dc = -1

        nr, nc = loc[0] + dr, loc[1] + dc

        # Bounds check
        if not (0 <= nr < len(maze) and 0 <= nc < len(maze[0])):
            print("Cannot move outside the maze.")
            continue

        # Wall check
        if maze[nr][nc] == '*':
            print("Cannot move into a wall.")
            continue

        # Apply valid move and re-display
        loc[0], loc[1] = nr, nc
        display_maze(maze, (loc[0], loc[1]))


if __name__ == "__main__":
    main()