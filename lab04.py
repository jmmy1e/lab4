from check_input import get_yes_no

def read_maze():
    maze_file = open("maze.txt", "r")
    file_lines = maze_file.readlines()
    one_dimension_list = []

    for line in file_lines:
        one_dimension_list.append(list(line.strip("\n")))
    return one_dimension_list


def find_start(maze):

    found_start = False
    row_index = 0
    for line in maze:
        column_index = 0
        for character in line:
            
            if character == "s":
                found_start = True
                break
                
            column_index += 1
        if found_start == True:
            break

        row_index += 1
    
    #print(f"Found start at " + str(row_index)+", " + str(column_index))
    return [row_index, column_index]

def display_maze(maze, loc):
    """
    ? Given the current maze re-init it with the users location
    ? Then display it
    """
    maze[loc[0]][loc[1]] = "X"
    for row in maze:
        current_buffer = ""
        for character in row:
           current_buffer = current_buffer + character
        print(current_buffer)

        





def main():
    """
    ? element access is [row][column]
    """

    while True:
        ## This is THE MAZE
        two_dimension_list = read_maze()
        ## This is the ORIGINAL START POSITION
        current_start_location = find_start(two_dimension_list)
        ORIGINAL_START_POINT = find_start(two_dimension_list)
        user_wants_to_quit = False

#
        #print("-Maze Solver-")
#

        #if maze[loc[0]][loc[1]] == 'f':
        #    print("Congratulations, you solved the maze!")
        #    break
        while True:
            ##? Print the initial maze state
            display_maze(two_dimension_list, current_start_location)

            move = input("1. Go North\n2. Go South\n3. Go East\n4. Go West\nEnter choice: ").strip().lower()
            if move not in ('1', '2', '3', '4',):
                print("Invalid input - enter 1-4")
                continue


            x_increment, y_increment = 0, 0
            """
            ! Directions Up & Down are inversed because of the way 2d matrix works
            ! To the human eye we see north as up but via index is the opposite
            """
            if move == '1':
                #  y value = 1 because they want up
               # y_increment = 1
               y_increment = -1
            elif move == '2':
                # y value = -1 because they want down
               # y_increment = -1
                y_increment = 1
            elif  move == '3':
                # x value = 1 because they want right
                x_increment = 1
            elif move == '4':
                # x value = -1 because they want left
                x_increment = -1

            # Before applying to the current location, first check if this would cause a collision
            current_maze_row_index, current_maze_column_index = current_start_location[0] + x_increment, current_start_location[1] + y_increment
            # Check the new respective location
            if(two_dimension_list[current_maze_row_index][current_maze_column_index] == " " or two_dimension_list[current_maze_row_index][current_maze_column_index] == "X" or two_dimension_list[current_maze_row_index][current_maze_column_index] == "s" ):
                # Because its in here this means its valid so take the current spot and assign it as whitespace
                # This is to restore its original state/character
                two_dimension_list[current_start_location[0]][current_start_location[1]] = " "

                # valid location and can move here
                #print(f"valid location, character is ({str(two_dimension_list[current_maze_row_index][current_maze_column_index])})" )

                # Set the current location to the new location
                current_start_location[0] = current_maze_row_index
                current_start_location[1] = current_maze_column_index

                #Insert the original 'S' position
                two_dimension_list[ORIGINAL_START_POINT[0]][ORIGINAL_START_POINT[1]] = "s"

                # Insert the indicator, overrides the previous
                two_dimension_list[current_maze_row_index][current_maze_column_index] = "X"

            elif(two_dimension_list[current_maze_row_index][current_maze_column_index] == "f"):
                two_dimension_list[current_start_location[0]][current_start_location[1]] = " "

                current_start_location[0] = current_maze_row_index
                current_start_location[1] = current_maze_column_index
                two_dimension_list[current_maze_row_index][current_maze_column_index] = "X"
                display_maze(two_dimension_list, current_start_location)
                print("Congratulations! You solved the maze.")
                break
            else:
                print(f"invalid location, you can't go there" )

        if get_yes_no("Would You like to play again?  "):
         print("Wants to play again")
        else:
         print("Goodbye!")
         break  
    

    





if __name__ == "__main__":
    main()


    # Up = north
    # Left = west
    # Right = east
    # Down = south