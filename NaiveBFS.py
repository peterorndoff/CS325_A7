"""
queue = []
visited = set()
while queue:
	me = queue.popleft()
	for every neighbor of me:
		if neighbor not in visited:
			visited.add(neighbor)
			queue.append(neighbor)
"""

from collections import deque as queue

row_vector = [-1, 0, 1, 0]
column_vector = [0, 1, 0, -1]


def minEffort(puzzle):
    visited_array = [[False for i in range(4)] for i in range(4)]

    row = 0
    column = 0
    minEffortBFS_helper(puzzle, visited_array, row, column)


def minEffortBFS_helper(puzzle, visited, row, column):
    q = queue()

    visited[row][column] = True
    q.append((row, column))

    while (len(q) > 0):

        node = q.popleft()
        y = node[1]
        x = node[0]
        print(puzzle[x][y], end=" ")

        for i in range(4):
            x_side = x + row_vector[i]
            y_side = y + column_vector[i]

            if valid_move(row, column, visited):
                visited[x_side][y_side] = True
                q.append((x_side, y_side))


def valid_move(row, column, visited):


    if visited[row][column] == True:
        return False

    if row < 0:
        return False

    if column < 0:
        return False

    if row >= 4:
        return False

    if column >= 4:
        return False

    else:
        return True


puzzle = [[1, 3, 5, 8], [2, 8, 3, 8], [3, 4, 5, 8]]
minEffort(puzzle)
