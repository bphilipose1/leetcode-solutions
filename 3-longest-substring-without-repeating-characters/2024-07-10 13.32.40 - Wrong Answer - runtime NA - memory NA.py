class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxlen = 0
        tempDict = {}
        count = 0
        while r < len(s):
            
            if s[r] not in tempDict:
                tempDict[s[r]] = 1
                count += 1
                r+= 1
            else:
                #clean up for next possible string
                if maxlen < count:
                    
                    maxlen = count
                    print(l, r, maxlen)
                l = r
                count = 0
                tempDict = {}
            
        return maxlen
                