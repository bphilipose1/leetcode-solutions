class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        maxRow = len(board)
        maxCol = len(board[0])
        direction = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        #dfs search
        def dfs(x, y, index, visited):
            #word is found
            if index == len(word):
                return True
            
            #invalid cell to go down
            if maxCol <= y or y < 0 or maxRow <= x or x < 0 or (x,y) in visited or board[x][y] != word[index]:
                return False
            
            visited.add((x,y))
            for dx, dy in direction:
                if dfs(x + dx, y + dy, index + 1, visited):
                    return True
            visited.remove((x, y)) #make it back to an option with backtrack
            return False


       
        for x in range(maxRow):
            for y in range(maxCol):
                temp = dfs( x, y, 0, set())
                if temp:
                    return True
        return False

