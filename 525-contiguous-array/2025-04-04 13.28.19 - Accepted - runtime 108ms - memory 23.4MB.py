class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        count_index = {0: -1}
        max_length = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_index:
                max_length = max(max_length, i - count_index[count])
            else:
                count_index[count] = i
            
        return max_length


