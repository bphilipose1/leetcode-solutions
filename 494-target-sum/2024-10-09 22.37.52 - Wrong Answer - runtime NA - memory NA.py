class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = []
        def rec(cur_sum, cur_sol, i):

            if cur_sum == target and cur_sol not in result:
                result.append(cur_sol.copy())
            if i == len(nums):
                return
            num = nums[i]
            #call where they add 1
            cur_sol.append(-num)
            rec(cur_sum - num, cur_sol, i + 1)

            #call where they minus 1
            cur_sol.pop()
            cur_sol.append(num)
            rec(cur_sum + num, cur_sol, i + 1)
            cur_sol.pop()
        rec(0, [], 0)
        print(result)
        return len(result)

            
            