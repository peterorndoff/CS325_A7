# Name: Peter Orndoff
# Description: Assignment 7, with help from Explorations and Group Assignment recommendations.
# Date: November 15th 2022

import heapq

def minEffort(puzzle):

    rows = len(puzzle) # Grabs length of Rows
    columns = len(puzzle[0]) # Grabs length of Columns
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # Directional vectors
    queue = [(0, 0, 0)] # Creates Queue

    while queue: # While queue is not empty

        current = heapq.heappop(queue)
        current_node = current[0]
        x_direction = current[1]
        y_direction = current[2]

        if len(puzzle) - 1 == x_direction and len(puzzle[0]) - 1 == y_direction:
            return current_node

        for i, j in directions:
            new_x_direction = x_direction + i # Calculates new X direction via current j indexes
            new_y_direction = y_direction + j # Calculates new Y direction via current i index

            if 0 <= new_x_direction < rows and 0 <= new_y_direction < columns and puzzle[new_x_direction][new_y_direction] is not None: # Comparative if move is valid:

                new = max(current_node, abs(puzzle[new_x_direction][new_y_direction] - puzzle[x_direction][y_direction])) # Grabs max of the current node/ Absolute of new node - currrent node.
                heapq.heappush(queue,(new, new_x_direction, new_y_direction)) # Pushes new, and it's x/y directions.

        puzzle[x_direction][y_direction] = None # Otherwise, set that index equal to None.
