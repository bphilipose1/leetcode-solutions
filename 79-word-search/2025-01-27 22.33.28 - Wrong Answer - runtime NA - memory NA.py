class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        target = word
        maxRow = len(board)
        maxCol = len(board[0])
        direction = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        #dfs search
        def dfs(board, x, y, index, visited = None):
            #create new visited set
            if visited is None:
                visited = set()
            if board[x][y] != target[index]: #this place doesnt make sense yet
                return False
            #record that node is now visited
            print('At', x, y, index, board[x][y])
            visited.add((x, y))

            #check if we found last letter of sequence so at index = len(target) - 1
            if index == len(target) - 1 and board[x][y] == target[index]:
                return True
            
            
            
            temp = False
            
            for dx, dy in direction:
                nx = dx + x
                ny = dy + y
                if maxCol > ny >= 0 and maxRow > nx >= 0 and (nx,ny) not in visited:
                    temp = dfs(board, nx, ny, index + 1, visited)
                    if temp:
                        return True
        
            return False
        
        for x in range(maxRow):
            for y in range(maxCol):
                print('starting/..', x, y)
                temp = dfs(board, x, y, 0, None)
                if temp:
                    return True
        return False

