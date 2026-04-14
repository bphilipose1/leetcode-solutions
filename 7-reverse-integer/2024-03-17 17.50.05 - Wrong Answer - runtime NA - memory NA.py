class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        tempNum = str(abs(x))
        newNum = ""
        for x in range(len(tempNum) - 1, -1, -1):
            newNum+=tempNum[x]
        result = int(newNum) * sign
        if result > (2**31 - 1) or result < -2**32:
            return 0
        return result