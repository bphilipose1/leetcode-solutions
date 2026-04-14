class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        letCount = {}
        for i in range(len(s)):
            if s[i] not in letCount:
                letCount[s[i]] = 1
            else:
                letCount[s[i]] = letCount[s[i]] + 1
            if t[i] not in letCount:
                letCount[t[i]] = -1
            else:
                letCount[t[i]] = letCount[t[i]] - 1
        return all(value == 0 for value in letCount.values())
        