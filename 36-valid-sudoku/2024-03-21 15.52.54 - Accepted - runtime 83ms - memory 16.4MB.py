class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] #make 9 row sets
        cols = [set() for _ in range(9)] #make 9 cols sets
        grid = [set() for _ in range(9)] #make 9 grid sets

        for x in range(9):
            for y in range(9):
                tempNum = board[x][y]
                if tempNum == '.':
                    continue
                gridNum = (y // 3) + 3 * (x // 3)
                if tempNum in rows[x] or tempNum in cols[y] or tempNum in grid[gridNum]:
                    return False
                else:
                    rows[x].add(tempNum)
                    cols[y].add(tempNum)
                    grid[gridNum].add(tempNum)

        return True
                