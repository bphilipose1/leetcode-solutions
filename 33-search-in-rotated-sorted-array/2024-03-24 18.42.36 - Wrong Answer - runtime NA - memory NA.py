class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m
        
        if target == nums[l]:
            return l

        if target <= nums[-1] and target >= nums[l]:
            r = len(nums)-1
        
        if target < nums[l] and target >= nums[0]:
            l = 0
        
        print("l: ", l)
        print("r: ", r)
        while l < r:
            m = (l + r) // 2
            if nums[r] == target:
                return m
            elif nums[m] < target: 
                l = m + 1
            else:
                r = m - 1

        return -1 
