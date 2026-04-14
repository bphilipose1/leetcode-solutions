class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        maxArea = 0

        def areaIsland(x, y):
            if x < 0 or x >= MAX_ROW or y < 0 or y >= MAX_COL or grid[x][y] == 0:
                return 0
            
            #set grid to 0 to be visited
            area = 1
            grid[x][y] = 0
            area += (areaIsland(x+1, y) + areaIsland(x-1, y) + areaIsland(x, y+1) + areaIsland(x, y-1)) #get areas from recursive calls

            return area
        for x in range(MAX_ROW):
            for y in range(MAX_COL):
                maxArea = max(areaIsland(x, y), maxArea) #update max Area
        
        return maxArea