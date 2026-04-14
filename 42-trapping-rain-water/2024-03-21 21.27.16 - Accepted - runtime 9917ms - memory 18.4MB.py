class Solution:
    def trap(self, height: List[int]) -> int:
        waterCount = 0
        for x in range(len(height)):
            if x == 0:
                lmax = 0
            else: 
                lmax = max(height[0:x])
            if x == len(height)-1:
                rmax = 0
            else:
                rmax = max(height[x+1:len(height)])
            tempCount = (min(rmax, lmax) - height[x])
            if tempCount < 0:
                tempCount = 0
            waterCount += tempCount
        return waterCount
            