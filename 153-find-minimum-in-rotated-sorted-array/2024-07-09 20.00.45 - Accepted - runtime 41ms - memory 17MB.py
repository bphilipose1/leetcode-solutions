class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curr_min = nums[0]
        while l < r:
            mid = int((l + r) / 2)
            print(nums[mid])
            curr_min = min(curr_min, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min(curr_min,nums[r])
        