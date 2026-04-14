class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MAXROW = len(grid)
        MAXCOL = len(grid[0])
        print(MAXROW, MAXCOL)
        maxArea = 0
        def recursivecount(x,y, count):
            if grid[x][y] == '1':
                count += 1
                recursivecount(x-1, y)
                recursivecount(x-1, y)
                

            
            

        for x in range(MAXROW):
            for y in range(MAXCOL):
                if grid[x][y] == '1':
                    tempSize = recursivecount(x,y, 0)
                    if tempSize > maxArea:
                        maxArea = tempSize
            