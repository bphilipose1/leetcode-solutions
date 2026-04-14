class Solution(object):
    def partitionString(self, s):
        biggestLength = 1
        temp = 0
        charCount = {}
        while temp < len(s):
            if not charCount.has_key(s[temp]): 
                charCount[s[temp]] = 1
                temp = temp + 1
            else:  
                biggestLength = biggestLength + 1
                charCount.clear()
        return biggestLength