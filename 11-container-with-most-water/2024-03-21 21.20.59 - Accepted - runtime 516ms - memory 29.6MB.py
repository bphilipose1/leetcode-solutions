class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        lptr = 0
        rptr = len(height)-1
        while lptr < rptr:
            tempWidth = abs(lptr-rptr)
            tempHeight = min(height[lptr], height[rptr])
            tempArea = tempWidth*tempHeight
            if tempArea > maxArea:
                maxArea = tempArea
                tempArea = 0
            if height[lptr] <= height[rptr]:
                lptr+=1
            else:
                rptr-=1

        return maxArea