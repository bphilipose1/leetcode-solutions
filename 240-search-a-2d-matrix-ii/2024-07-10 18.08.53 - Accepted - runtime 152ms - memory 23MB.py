class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        MAXROW, MAXCOL = len(matrix), len(matrix[0])
        for row in matrix:
            #Binary search in the row
            l, r = 0, int((len(row) - 1))
            while l <= r:
                mid = int((l + r) / 2)
                if row[mid] == target:
                    return True
                if row[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return False

