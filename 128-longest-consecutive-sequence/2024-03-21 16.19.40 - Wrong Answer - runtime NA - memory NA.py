class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sortedNums = sorted(nums)
        print(sortedNums)
        consCount = 1
        maxCount = 1
        prevNum = sortedNums[0]
        for x in range(1, len(sortedNums)):
            if (sortedNums[x] - prevNum) == 1:
                consCount+=1
                prevNum = sortedNums[x]
            else:
                if consCount > maxCount:
                    maxCount = consCount
                consCount = 1
                prevNum = sortedNums[x]
        return max(maxCount, consCount)