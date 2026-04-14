class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1
        
        result *= sign

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
