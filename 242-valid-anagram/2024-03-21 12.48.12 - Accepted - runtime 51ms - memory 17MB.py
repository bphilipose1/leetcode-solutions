from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqDict1 = Counter(t)
        freqDict2 = Counter(s)
        if freqDict1 != freqDict2:
            return False
        return True

        