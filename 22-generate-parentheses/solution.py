class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        abslen = 2*n
        def recursivefunc(left, right, temp):
            if len(temp) == abslen:
                result.append(temp)
                return
            if left < n:
                recursivefunc(left + 1, right, temp + '(')
            if right < left:
                recursivefunc(left, right + 1, temp + ')')
        recursivefunc(0,0,'')
        return result
            