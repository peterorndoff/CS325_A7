# Name: Peter Orndoff
# Assignment: Homework #7 - Graph Algorithms I
# Date: November 14th 2022

def minEffort(puzzle):

    distance_array = [[None]*len(puzzle) for items in range(len(puzzle))]
    visited_array = [[False]*len(puzzle) for items in range(len(puzzle))]

    visited_array[0][0] = True
    dijkstras(puzzle, distance_array, visited_array)

    return distance_array


def dikstras(puzzle):


    


"""def dijkstras(puzzle, distance_array, visited_array):

    i = 0
    j = 0

    # [ROW][COLUMN]

    right = [i][j+1]
    left = [i][j-1]
    up = [i+1][j]
    down = [i-1][j]

    puzzle_size = len(puzzle) - 1

    start = puzzle[i][j]

    while distance_array[len(distance_array)][len(distance_array)] is False:

        if i == 0: # At Left edge of puzzle: UP, DOWN, RIGHT
            if j == 0: # Checks if at top left corner of puzzle:

                if puzzle[i][j+1] < puzzle[i-1][j]: # Column 1 Comparative Row under.


                # Then can only go right or down.

            if j == puzzle_size: # Checks if at bottom left corner
                # Then can only go right or up.

            # Otherwise, can go up, down, right.

        if i == puzzle_size: # At Right edge of puzzle: Can only go UP DOWN or RIGHT
            if j == puzzle_size:
                # Can only go LEFT or DOWN."""

"""
You are given a 3-D puzzle. The length and breadth of the puzzle is given by a 2D matrix
puzzle[m][n].

- The height of each cell is given by the value of each cell.
- The value of puzzle[row][column] give the height of the cell [row][column].

= You are at [0][0] cell, and you want to reach to the bottom right cell [m-1][n-1] which is the destination cell.
- You can move either up, down, left, or right.

Write an algorithm to reach the destination cell with minimal effort.
How effort is defined: The effort of route is the maximum absolute difference between two
consecutive cells.

How effort is defined:

The effort of route is the maximum absolute difference between two consecutive cells.
If a route requires us to cross heights: 1, 3, 4, 6, 3, 1
The absolute differences between consecutive cells is: |1-3| = 2, |3-4|=1, |4-6|=2,
|6-3|=3, |3-1|=2; this gives us the values: {2, 1, 2, 3, 2}. The maximum value of
these absolute differences is 3. Hence the effort required on this path will be: 3

"""

puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))