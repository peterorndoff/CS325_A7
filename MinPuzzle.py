import heapq

def minEffort(heights):

   r,c=len(heights),len(heights[0])
   queue=[(0,0,0)]

   while queue:

      cur=heapq.heappop(queue)
      c_eff=cur[0]
      x=cur[1]
      y=cur[2]

      if x==r-1 and y==c-1:
         return c_eff

      if heights[x][y]=="":
         continue

      for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
         newx=x+dx
         newy=y+dy
         if 0<=newx<r and 0<=newy<c and heights[newx][newy]!="":

            eff = max(c_eff, abs(heights[newx][newy] - heights[x][y]))
            heapq.heappush(queue,(eff, newx, newy))

      heights[x][y]=""
