class NumArray:

    def __init__(self, nums: List[int]):
        self.base_nums = nums #holds the normal values

        #create the prefix array
        self.cum_sum_nums = [0] * len(nums)
        temp_sum = 0
        for idx, val in enumerate(nums):
            temp_sum += val
            self.cum_sum_nums[idx] = temp_sum
                        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cum_sum_nums[right]
        return self.cum_sum_nums[right] - self.cum_sum_nums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)