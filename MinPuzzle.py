# Name: Peter Orndoff
# Assignment: Homework #7 - Graph Algorithms I
# Date: November 14th 2022

def minEffort(puzzle):

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




