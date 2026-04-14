class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numCount = {}
        longestCount = 0
        currCount = 0
        i = 1
        while i < len(s):
            if s[i] in numCount:
                if currCount > longestCount:
                    longestCount = currCount
                i = numCount[s[i]]
                currCount = 0
                numCount.clear()
            else:
                numCount[s[i]] = i
                currCount = currCount + 1
            i = i + 1
        return longestCount
        