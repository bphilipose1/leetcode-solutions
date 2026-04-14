class Solution(object):
    def partitionString(self, s):
        biggestLength = 1
        tempLength = 0
        tempStart = 0
        tempEnd = 0
        charCount = {}
        while tempEnd < len(s):
            if tempStart == tempEnd:
                charCount[s[tempStart]] = 1
                tempEnd = tempEnd + 1
                tempLength = 1
            else:
                if not charCount.has_key(s[tempEnd]): 
                    charCount[s[tempEnd]] = 1
                    tempLength = tempLength + 1
                    tempEnd = tempEnd + 1
                else: 
                    tempStart = tempEnd 
                    biggestLength = biggestLength + 1
                    charCount.clear()
        return biggestLength