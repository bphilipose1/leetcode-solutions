class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = []
        def rec(cur_sum, cur_sol, i):

            if cur_sum == target and i == len(nums) and cur_sol not in result:
                result.append(cur_sol.copy())
                return
            if i == len(nums):
                return
            print(cur_sol, i)
            num = nums[i]
            #call where they add 1
            cur_sol.append(-num)
            rec(cur_sum - num, cur_sol, i + 1)

            #call where they minus 1
            cur_sol.pop()
            cur_sol.append(num)
            rec(cur_sum + num, cur_sol, i + 1)
        rec(0, [], 0)
        return len(result)

            
            