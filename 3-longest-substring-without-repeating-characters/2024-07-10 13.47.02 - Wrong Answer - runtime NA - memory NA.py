class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        finalCount = 0
        count = 0
        for r in range(len(s)):
            #if duplicate found
            if s[r] in char_dict:
                #check if temp count is greater than current count
                if count > finalCount:
                    finalCount = count
                #put r back one to the position after the first of the two redundant character 
                r = char_dict[s[r]] + 1

                #reset the count, and set
                count = 0
                charset = {}
            else:
                #most recent indice
                char_dict[s[r]] = r
                #increase temp string size
                count += 1
        return finalCount
            
                
                