class Solution:
    def backtrack(self, nums, start, path, ans):
        ans.append(path.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, ans)
            path.pop() 

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans

    