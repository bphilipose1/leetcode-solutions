class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo_matrix = [[0] * n for _ in range(m)]
        memo_matrix[m-1][n-1] = 1 #only one unique path starting at finish
        MAX_ROW = m
        MAX_COL = n

        for row in range(MAX_ROW - 1, -1, -1):    
            for col in range(MAX_COL - 1, -1, -1):    
                if row == (m-1) and col == (n-1):
                    continue
                #GET VALUE BELOW (if exists)
                if (row + 1) >= MAX_ROW:
                    below_val = 0
                else: #retrieve its value
                    below_val = memo_matrix[row + 1][col]
                
                #GET VALUE RIGHT (if exists)
                if (col  + 1) >= MAX_COL:
                    right_val = 0
                else: #retrieve its value
                    right_val = memo_matrix[row][col + 1]

                #store the two possible paths together
                new_val = below_val + right_val
                memo_matrix[row][col] = new_val
                




        #return the value of unique paths starting from current row and col
        return memo_matrix[0][0]

    