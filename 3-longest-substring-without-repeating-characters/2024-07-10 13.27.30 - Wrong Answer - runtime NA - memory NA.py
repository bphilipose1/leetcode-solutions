class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxlen = 0
        tempDict = {}
        while r < len(s):
            if s[r] not in tempDict:
                tempDict[s[r]] = 1
            else:
                #clean up for next possible string
                if maxlen < (r - l):
                    maxlen = (r - l)
                l = r
                tempDict = {}
            r+=1
        return maxlen
                