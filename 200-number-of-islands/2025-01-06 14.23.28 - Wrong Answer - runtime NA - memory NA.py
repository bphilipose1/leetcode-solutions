class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        islandCount = 0
        def removeIsland(x, y):
            #chceck if x and y are out of bounds and an island still
            if MAX_ROW <= x or MAX_COL <= y or grid[x][y] == '0': 
                return
            #set island marker to 0 to not recount island square
            grid[x][y] = '0'

            #rec call to surrounding areas
            removeIsland(x+1,y)
            removeIsland(x-1,y)
            removeIsland(x,y+1)
            removeIsland(x,y-1)


        for x in range(MAX_ROW):
            for y in range(MAX_COL):
                print(x, y, grid[x][y])
                if grid[x][y] == '1':
                    removeIsland(x, y)
                    islandCount += 1
        
        return islandCount