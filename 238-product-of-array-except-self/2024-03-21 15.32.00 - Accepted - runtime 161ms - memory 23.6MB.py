class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultList = []
        totalProduct = 1
        totalProductWithZero = 1
        zeroCount = 0
        for val in nums:
            totalProductWithZero*=val
            zeroCount+=1
            if val != 0:
                zeroCount-=1
                totalProduct*=val

        if zeroCount > 1:
            return [0]*len(nums)
        for x in range(0, len(nums)):
            if nums[x] == 0:
                resultList.append(totalProduct)
            else:
                resultList.append(int(totalProductWithZero/nums[x]))
        return resultList
            