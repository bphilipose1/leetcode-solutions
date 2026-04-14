class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        frontPtr = 0
        endPtr = len(numbers) - 1
        while (numbers[frontPtr] + numbers[endPtr]) != target:
            tempVal = numbers[frontPtr] + numbers[endPtr]
            if tempVal > target:
                endPtr-=1
            elif tempVal < target:
                frontPtr+=1
        return [frontPtr+1, endPtr+1]