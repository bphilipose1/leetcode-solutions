class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, lCol, rRow, rCol = 0,0,len(matrix) - 1, len(matrix[0]) - 1
        while lRow <= rRow:
            mid = int(rRow - lRow / 2)
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                #binary search in the row
                print('hit row: ', mid)
                while lCol <= rCol:
                    mid1 = int(rCol - lCol / 2)
                    if matrix[mid][mid1] == target:
                        print('hit col: ', mid1)
                        return True
                    elif matrix[mid][mid1] < target:
                        lCol = mid1 + 1
                    else:
                        rCol = mid1 - 1
                return False
            elif matrix[mid][0] < target:
                lRow = mid + 1
            else:
                rRow = mid - 1
        return False