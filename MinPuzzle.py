# Name: Peter Orndoff
# Description: Assignment 7, with help from Explorations and Group Assignment recommendations.
# Date: November 15th 2022

import heapq


def minEffort(puzzle):

    queue = [(0, 0, 0)]  # Creates Queue
    rows = len(puzzle)  # Grabs length of Rows
    columns = len(puzzle[0])  # Grabs length of Columns
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # Directional vectors

    queue = [(0, 0, 0)]  # Creates Queue
    current_index = 0
    x_queue_index = 1
    y_queue_index = 2

    while queue:  # While queue is not empty

        current = heapq.heappop(queue)
        current_node = current[current_index]
        x_direction = current[x_queue_index]
        y_direction = current[y_queue_index]

        if puzzle[x_direction][y_direction] is None: # If None is found, continue with the while loop.
            continue

        if len(puzzle) - 1 == x_direction and len(puzzle[0]) - 1 == y_direction: # Base case for while loop exit.
            return current_node # Returns min effort

        for i, j in directions:

            new_x_direction = x_direction + i  # Calculates new X direction via current j indexes
            new_y_direction = y_direction + j  # Calculates new Y direction via current i index

            if  puzzle[new_x_direction][new_y_direction] is not None and 0 <= new_x_direction < rows\
                    and 0 <= new_y_direction < columns:  # Comparative if move is valid:

                new = max(current_node, puzzle[new_x_direction][new_y_direction] - puzzle[x_direction][
                    y_direction])  # Grabs max of the current node/ Absolute of new node - currrent node.
                heapq.heappush(queue, (new, new_x_direction, new_y_direction))  # Pushes new, and it's x/y directions.

        puzzle[x_direction][y_direction] = None  # Set that index equal to None.
