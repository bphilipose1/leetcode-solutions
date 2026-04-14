class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        for index, value in enumerate(nums):
            compliment = target - value

            if compliment in indexDict:
                return [indexDict[compliment], index]
            else:
                indexDict[value] = index
        return -1
                

        