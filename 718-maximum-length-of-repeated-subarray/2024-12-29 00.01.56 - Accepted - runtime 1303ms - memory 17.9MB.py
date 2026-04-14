class Solution:
    from collections import Counter
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #create a 2d matrix to store max length for matching subarrays max length at that point
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        max_length = 0

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if nums1[i - 1] == nums2[j - 1]: #offset for including 0
                    dp[j] = dp[j - 1] + 1 #carry over prev solution to new one and increment
                    max_length = max(max_length, dp[j]) #update current max
                else:
                    dp[j] = 0
        return max_length

