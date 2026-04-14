class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ending_at_i = nums[0]
        best_ever = nums[0]
        for i in nums[1:]:
            if best_ending_at_i < 0:
                best_ending_at_i = i
            else:
                best_ending_at_i += i
            if best_ending_at_i > best_ever:
                best_ever = best_ending_at_i
        return best_ever