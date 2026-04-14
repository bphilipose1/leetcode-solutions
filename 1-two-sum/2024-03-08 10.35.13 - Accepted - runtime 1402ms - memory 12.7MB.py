class Solution(object):
    
    def findNumIndex(self, inputList, start, target):
        for i in range(start, len(inputList)):
            if inputList[i] == target:
                return i
        return -1

    def twoSum(self, nums, target):

        for i in range(len(nums)):
            look = (target - nums[i])
            arrSize = len(nums) - 1
            retVal = self.findNumIndex(nums, i+1, look)
            if retVal != -1:
                return [i, retVal]

