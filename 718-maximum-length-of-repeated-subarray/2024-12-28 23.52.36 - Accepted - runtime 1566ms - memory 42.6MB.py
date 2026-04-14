class Solution:
    from collections import Counter
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #create a 2d matrix to store max length for matching subarrays max length at that point
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)] #n+1 rows and cols to account for 0 meaning no match
        max_length = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]: #offset for including 0
                    dp[i][j] = dp[i - 1][j - 1] + 1 #carry over prev solution to new one and increment
                    max_length = max(max_length, dp[i][j]) #update current max
        
        return max_length

