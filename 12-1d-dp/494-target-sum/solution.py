class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def rec(cur_sum, i):
            if i == len(nums):
                return 1 if cur_sum == target else 0
            if (cur_sum, i) in memo:
                return memo[(cur_sum, i)]
            
            
            add = rec(cur_sum + nums[i], i + 1)
            subtract = rec(cur_sum - nums[i], i + 1)
            
            # Store the result in the memoization dictionary
            memo[(cur_sum, i)] = add + subtract
            return memo[(cur_sum, i)]
        return rec(0, 0)
