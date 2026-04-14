class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        MAX_ROW = len(matrix)
        MAX_COL = len(matrix[0])
        prev_path = {}
        def rec(row, col):

            #check out of bounds error, or if cell is already in path
            if row >= MAX_ROW or col >= MAX_COL: 
                return 0

            if (row, col) in prev_path: #has already been done just get from memory
                return prev_path[(row, col)]

            longest_path = 1
            
            left, right, up, down = 0, 0, 0, 0
            #return longest path from that point
            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= r < MAX_ROW and 0 <= c < MAX_COL and matrix[r][c] > matrix[row][col]:
                    longest_path = max(longest_path, 1 + rec(r, c))

            #memoize current recursion tree
            prev_path[(row, col)] = longest_path
            return longest_path

        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                rec(row, col)
        return max(prev_path.values())

