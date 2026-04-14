class Solution(object):
    def removeDuplicates(self, nums):
        lastElement = nums[0]
        uniqueCount = 0
        currArrSize = len(nums) - 1
        iter = 1
        while iter <= currArrSize:
            
            if lastElement == nums[iter]:
                nums.remove(nums[iter])
                currArrSize = currArrSize - 1
            else:
                uniqueCount = uniqueCount + 1
                lastElement = nums[iter]
                iter = iter + 1

            
        