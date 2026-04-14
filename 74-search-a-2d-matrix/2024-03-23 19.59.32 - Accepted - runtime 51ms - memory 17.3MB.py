class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowStart = 0
        rowEnd = len(matrix)-1
        while rowStart <= rowEnd:
            midRow = (rowStart + rowEnd) // 2
            if matrix[midRow][0] <= target and matrix[midRow][-1] >= target:
                x = matrix[midRow]
                start = 0
                end  = len(x)-1
                while start <= end:
                    mid = (start + end) // 2
                    if x[mid] == target:
                        return True
                    elif x[mid] < target:
                        start = mid + 1
                    elif x[mid] > target:
                        end = mid - 1
                return False
            elif matrix[midRow][0] > target:
                rowEnd = midRow - 1
            elif matrix[midRow][-1] < target:
                rowStart = midRow + 1

            
        
        
        