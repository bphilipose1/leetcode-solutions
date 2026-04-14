class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            if x[0] <= target and x[-1] >= target:
                start = 0
                end  = len(x)-1
                while start < end:
                    mid = (start + end) // 2
                    if x[mid] == target:
                        return True
                    elif x[mid] > target:
                        start = mid + 1
                    elif x[mid] < target:
                        end = mid - 1
                return False
                    

            
        
        
        