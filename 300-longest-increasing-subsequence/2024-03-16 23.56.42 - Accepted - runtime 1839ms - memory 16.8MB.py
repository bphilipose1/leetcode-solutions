class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        numList = [1] * len(nums)

        for i in range (len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    numList[i] = max(numList[i], 1 + numList[j])

        return max(numList)