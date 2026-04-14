class Solution(object):
    def containsDuplicate(self, nums):
        numCounts = {}
        for i in range(len(nums)):
            if nums[i] not in numCounts:
                numCounts[nums[i]] = 1
            else:
                return True
        return False