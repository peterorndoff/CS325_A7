import heapq


def solve(heights):

   rows = len(heights[0])
   columns  = len(heights)
   queue = [(0,0,0)]

   while queue:

      current_node = heapq.heappop(queue)
      c_eff = current_node[0]
      x = current_node[1]
      y = current_node[2]

      if x == rows-1 and y == columns-1:

         return c_eff

      for change_x , change_Y in [[1,0],[-1,0],[0,1],[0,-1]]:

         newx = x + change_x
         newy = y + change_Y

         if 0 <= newx < rows and 0 <= newy < columns and heights[newx][newy]!="":

            eff = max(c_eff, abs(heights[newx][newy] - heights[x][y]))
            heapq.heappush(queue,(eff, newx, newy))

      heights[x][y]=""

matrix = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(solve(matrix))