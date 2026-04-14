class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def recursivePar(remainder = 0, stack = [], result = ''):
            bigResult = []
            if remainder > 0:
                remainder-=1
                stack.append('(')
                result += '('
                tempRes = recursivePar(remainder, stack, result)
                if tempRes:
                    bigResult.append(tempRes)
            if stack:
                stack.pop()
                result+=')'
                tempRes = recursivePar(remainder, stack, result)
                if tempRes:
                    bigResult.append(tempRes)
            return bigResult
        recursivePar(n, stack, '')


    