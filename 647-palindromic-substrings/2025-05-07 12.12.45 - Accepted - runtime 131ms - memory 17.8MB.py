class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[right] == s[left]:
                count += 1 #this accounts for current palindrome
                left -= 1
                right += 1
            return count
        
        total = 0
        for i in range(len(s)):
            total += expand(i, i)
            total += expand(i, i+1)

        return total
        