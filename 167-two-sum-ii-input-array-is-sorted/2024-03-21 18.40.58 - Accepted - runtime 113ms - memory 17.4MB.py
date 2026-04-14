class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexDict = {}
        for index, value in enumerate(numbers):
            compliment = target - value
            if compliment in indexDict:
                return [indexDict[compliment]+1, index+1]
            else: 
                indexDict[value] = index