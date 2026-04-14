class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #convert each time into total minutes
        minArr = [0]* (60*24)
        for time in timePoints:
            hr, mn = time.split(':')
            mn = int(mn)
            mn += int(hr) * 60
            minArr[mn] += 1
        #go through the array and store the non 0 indexes
        focusArr = []
        for idx, num in enumerate(minArr):
            if num != 0:
                focusArr.append(idx)
            if num >= 2: #same time is the min
                return 0
        
        #interate through array and find smallest differce
        minDiff = min(focusArr[-1] - focusArr[0], focusArr[0] + (24*60 - focusArr[-1]))
        for i in range(1, len(focusArr)):
            temp_diff1 = abs(focusArr[i] - focusArr[i-1])
            temp_diff2 = abs(focusArr[i-1] + (24*60 - focusArr[i]))

            temp_diff = min(temp_diff1, temp_diff2)
            
            minDiff = min(minDiff, temp_diff)
        return minDiff