class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = int(r + l / 2)
            print(mid)
            if nums[mid] < target:
                l = mid  + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1