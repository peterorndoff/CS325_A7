# Name: Peter Orndoff
# Description: Assignment
# Date: November 15th 2022

import heapq

def minEffort(puzzle):

    rows = len(puzzle)
    columns = len(puzzle[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = [(0, 0, 0)]

    while queue:

        current = heapq.heappop(queue)
        current_node = current[0]
        x_direction = current[1]
        y_direction = current[2]

        if len(puzzle) - 1 == x_direction and len(puzzle[0]) - 1 == y_direction:
            return current_node

        if puzzle[x_direction][y_direction] is None:
            continue

        for i, j in directions:
            new_x_direction = x_direction + i
            new_y_direction = y_direction + j

            if 0 <= new_x_direction < rows and 0 <= new_y_direction < columns and puzzle[new_x_direction][new_y_direction] is not None:

                new = max(current_node, abs(puzzle[new_x_direction][new_y_direction] - puzzle[x_direction][y_direction]))
                heapq.heappush(queue,(new, new_x_direction, new_y_direction))

        puzzle[x_direction][y_direction] = None
