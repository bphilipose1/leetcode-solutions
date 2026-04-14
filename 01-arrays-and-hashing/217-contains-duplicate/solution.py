class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqDict = {}
        for x in nums:
            if x in freqDict:
                return True
            else:
                freqDict[x] = 1
        return False
        