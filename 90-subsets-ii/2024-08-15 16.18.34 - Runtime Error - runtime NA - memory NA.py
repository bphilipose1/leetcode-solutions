class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = nums.sort()
        def recFunc(start, perm):
            if start >= len(nums):
                results.append(perm.copy())
                return
            
            #inclusion case
            perm.append(nums[start])
            recFunc(start + 1, perm)

            #skip all the duplicates after it for inclusion exclusion
            x = start
            while x < len(nums) - 1 and nums[x] == nums[x+1]:
                x += 1   
                       
            #exclusion case
            perm.pop()
            recFunc(x + 1, perm)
        
        recFunc(0, [])
        return results
