class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def rec(cur_sum, i):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            return rec(cur_sum + nums[i], i + 1) + rec(cur_sum - nums[i], i + 1)
        return rec(0, 0)
