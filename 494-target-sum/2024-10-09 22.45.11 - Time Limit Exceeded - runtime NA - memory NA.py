class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result_count = 0
        def rec(cur_sum, i):
            nonlocal result_count
            if i == len(nums):
                if cur_sum == target:
                    result_count += 1
                return
            if i == len(nums):
                return
            num = nums[i]
            #call where they add 1
            rec(cur_sum - num, i + 1)

            #call where they minus 1
            rec(cur_sum + num, i + 1)
        rec(0, 0)
        print(result_count)
        return result_count

            
            