class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        matrix = [["" for _ in range(len(s))] for _ in range(numRows)]
        x, y = 0, 0
        direction = -1  

        for char in s:
            matrix[x][y] = char
            if x == 0:
                direction = -1
            elif x == numRows - 1:
                direction = 1
            
            if direction == -1:
                x += 1  # Move down
            else:
                x -= 1  # Move diagonally up
                y += 1  # Move right when moving up

        result = "".join(["".join(row) for row in matrix if row])
        return result