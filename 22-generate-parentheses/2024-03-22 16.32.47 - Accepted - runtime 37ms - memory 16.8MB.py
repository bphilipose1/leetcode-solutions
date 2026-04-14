class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def recursivePar(left, right, result, maxLen):
            if len(result) == maxLen:
                ans.append(result)
                return
            if left < n:
                recursivePar(left+1, right, result+'(', maxLen)
            if right < left:
                recursivePar(left, right+1, result+')', maxLen)
        ans = []
        recursivePar(0,0,'',2*n)
        return ans


    