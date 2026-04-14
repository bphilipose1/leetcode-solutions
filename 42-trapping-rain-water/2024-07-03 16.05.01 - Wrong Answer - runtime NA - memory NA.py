class Solution:
    def trap(self, height: List[int]) -> int:
        #so left pointer and right pointer start at 0 index
        l, r = 0, 0
        totalRain = 0
        # right moves until either case
        while ((l < len(height) - 1) and (r < len(height) - 1)):
            r += 1
            while r < len(height) - 1 and height[l] > height[r]:
                r+=1
            # case1 if finds a height greater than or equal to left height
            if height[l] <= height[r]:
                #calculate the water between
                min_height_temp = min(height[l], height[r])
                tempRainAmnt = 0
                for x in range(l+1, r):
                    tempRainAmnt += (min_height_temp - height[x])
                totalRain += tempRainAmnt
                print(totalRain, l, r)
                l = r
            else:
                l += 1
                r = l + 1

            #reset left and right pointer to the right height
            
        return totalRain
    




            