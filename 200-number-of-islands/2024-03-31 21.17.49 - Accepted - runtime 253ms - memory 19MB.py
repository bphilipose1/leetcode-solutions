class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        MAXROW = len(grid) 
        MAXCOL = len(grid[0]) 
        def claimIsland(row, col):
            #hit border, or edge of island, kill recusive call off
            if row >= MAXROW or col >= MAXCOL or row < 0 or col < 0 or grid[row][col] == "0" or grid[row][col] == "2":
                return
            
            #if it is a connected Island
            if grid[row][col] == "1":
                grid[row][col] = "2"
            
            #check surrounding squares
            claimIsland(row + 1, col)
            claimIsland(row, col+1)
            claimIsland(row-1, col)
            claimIsland(row, col-1)
        islandCount = 0
        for x in range(MAXROW):
            for y in range(MAXCOL):
                print(grid[x][y])
                if grid[x][y] == "1":
                    islandCount += 1

                    claimIsland(x, y)                 

        return islandCount


