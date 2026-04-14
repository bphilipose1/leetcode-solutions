class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = []
        def rec(cur_sum, cur_sol, i):

            if cur_sum == target and i >= len(nums) and cur_sol not in result:
                result.append(cur_sol.copy())
                return
            if i > len(nums):
                return
            
            #call where they add 1
            cur_sol.append('-1')
            rec(cur_sum + 1, cur_sol, i + 1)

            #call where they minus 1
            cur_sol.pop()
            cur_sol.append('+1')
            rec(cur_sum - 1, cur_sol, i + 1)
        rec(0, [], 1)
        return len(result)

            
            