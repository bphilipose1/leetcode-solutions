class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #convert each time into total minutes
        minArr = []
        for time in timePoints:
            hr, mn = time.split(':')
            mn = int(mn)
            mn += int(hr) * 60
            minArr.append(mn)
        #sort the times
        minArr.sort()
        print(minArr)
        #interate through array and find smallest differce
        minDiff = abs(minArr[-1] - minArr[0])
        for i in range(1, len(minArr)):
            temp_diff1 = abs(minArr[i] - minArr[i-1])
            temp_diff2 = abs(minArr[i-1] + (24*60 - minArr[i]))

            temp_diff = min(temp_diff1, temp_diff2)
            
            minDiff = min(minDiff, temp_diff)
        return minDiff