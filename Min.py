

def djik(puzzle):

    visited = [[False] * len(puzzle) for items in range(len(puzzle))]  # If array has been visited set to True
    unvisited = [[True] * len(puzzle) for items in range(len(puzzle))]  # If array is unvisited True
    distance = [[None] * len(puzzle) for items in range(len(puzzle))]  # Distance 2d grid from [0][0]


    row = 0
    column = 0

    counter = 0


    while counter < len(puzzle)*2 -2:  # While all nodes haven't been visited.

        # 1) Take current node and remove it from unvisisted and append it to visited.

        visited[row][column] = True  # Sets visited node
        unvisited[row][column] = False  # Sets unvisited Node to 0
        distance[row][column] = puzzle[row][column]  # Sets initial Node distance to 0
        counter += 1

        # 2) Check nodes around current node. Calculate Distances.


        if row == 0: #If at top of grid:

            if column == 0:
                # Move right or down.
                right_node = puzzle[row][column+1] # Grabs value of right node.
                bottom_node = puzzle[row+1][column] # Grabs value of left node.

                right_distance = right_node - distance[row][column]
                bottom_distance = bottom_node - distance[row][column]

                distance[row][column+1] = right_distance
                distance[row+1][column] = bottom_distance

                if right_distance > bottom_distance: # If right distance is smaller than bottom:
                    row += 1
                else:
                    column += 1

            if column == len(puzzle) - 1:
                pass
                # Move down or left.

        if row == len(puzzle) - 1: # If at bottom of grid.
            pass
        if column == 0: # Left side of grid:
            # right, left, up


        if column == len(puzzle) - 1: # If at right side of grid.
            pass
        else:
            pass
            # Can move all directions.





puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(djik(puzzle))