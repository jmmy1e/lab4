"""
LAB #4
    09/15/2025
    Student 1: Jimmy Le
    Student 2: Daniel McCray

    File IO: Create a program that allows the user to solve a maze that is read in from a file. The user will 
    begin at the starting point (‘s’) of the maze and will be able to move up, down, left, or right to 
    move through the maze. When the user reaches the finish (‘f’), they have solved the maze
"""
def read_maze(file_name):
    """Read a maze from a file and return it as a list of lists."""
    maze = []
    with open(file_name, 'r') as file:
        for line in file:
            maze.append(list(line.strip()))
    return maze

def find_start(maze):
    """Find the starting position 's' in the maze."""
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 's':
                return (i, j)
    return None

def display_maze(maze, loc):
    """Display the maze with the current location marked."""
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == loc:
                if maze[i][j] == 's':
                    print('X', end='')  # Show X at starting position initially
                else:
                    print('X', end='')  # Mark current location elsewhere
            else:
                print(cell, end='')
        print()


def main():
    maze = read_maze("maze.txt")
    start = find_start(maze)
    display_maze(maze, start)

    loc = [start[0], start[1]]
    while True:
        if maze[loc[0]][loc[1]] == 'f':
            print("Congratulations, you solved the maze!")
            break
        move_input = input("1. Go North\n2. Go South\n3. Go East\n4. Go West\nEnter choice: ").strip().lower()
        if move_input not in ('1', '2', '3', '4', 'n', 's', 'e', 'w'):
            print("Invalid input - enter 1-4 or n/s/e/w.")
            continue
        mapping = {'1': 'n', '2': 's', '3': 'e', '4': 'w'}
        move = mapping.get(move_input, move_input)
        dr, dc = 0, 0
        if move == 'n' or move == '1':
            dr = -1
        elif move == 's' or move == '2':
            dr = 1
        elif move == 'e' or move == '3':
            dc = 1
        elif move == 'w' or move == '4':
            dc = -1

        nr, nc = loc[0] + dr, loc[1] + dc
        if not (0 <= nr < len(maze) and 0 <= nc < len(maze[0])):
            print("Cannot move outside the maze.")
            continue
        if maze[nr][nc] == '*':
            print("Cannot move into a wall.")
            continue
        loc[0], loc[1] = nr, nc
        display_maze(maze, (loc[0], loc[1]))


if __name__ == "__main__":
    main()