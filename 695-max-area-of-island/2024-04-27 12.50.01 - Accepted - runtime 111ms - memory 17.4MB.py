class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MAXROW = len(grid)
        MAXCOL = len(grid[0])
        maxArea = 0
        def recursivecount(x,y,count):
            if x < 0 or y < 0 or x >= MAXROW or y >= MAXCOL or grid[x][y] == 0:
                #print(x,y,'mis')
                return count
            if grid[x][y] == 1:
                #print(x,y,'hit')
                grid[x][y] = 0
                return 1 + recursivecount(x-1, y, count) + recursivecount(x+1, y, count) + recursivecount(x, y-1, count) + recursivecount(x, y+1, count)


            
            

        for x in range(MAXROW):
            for y in range(MAXCOL):
                if grid[x][y] == 1:
                    tempSize = recursivecount(x,y,0)
                    print('visit: [',x,'][',y,']', tempSize)
                    if tempSize > maxArea:
                        maxArea = tempSize
        return maxArea
            