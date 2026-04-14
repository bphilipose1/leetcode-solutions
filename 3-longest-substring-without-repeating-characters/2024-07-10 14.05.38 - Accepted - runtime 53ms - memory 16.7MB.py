class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = set()
        finalCount = 0
        l = 0
        for r in range(len(s)):
        
            while s[r] in char_dict:
                #put r back one to the position after the first of the two redundant character 
                char_dict.remove(s[l])
                l+=1
            finalCount = max(r-l+1, finalCount)
            char_dict.add(s[r])

        return finalCount
            
                
                