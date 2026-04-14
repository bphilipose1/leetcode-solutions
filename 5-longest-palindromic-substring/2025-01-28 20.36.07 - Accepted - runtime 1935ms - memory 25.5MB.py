class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0
        max_len = 1

        # Initialize single characters as palindromes of length 1
        for i in range(n):
            dp[i][i] = True
            if max_len == 1:
                start = i
                end = i

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                max_len = 2
                start = i
                end = i + 1

        # Check substrings of length greater than or equal to 3
        for l in range(3, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    max_len = l
                    start = i
                    end = j

        return s[start:end+1]