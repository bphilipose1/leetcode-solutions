class Solution:
    def isValid(self, s: str) -> bool:
        parList = []
        parenthPair = {')' : '(', ']' : '[', '}' : '{'}
        for parenth in s:
            if parenth not in parenthPair:
                parList.append(parenth)
            else:
                if len(parList) != 0 and parList[-1] == parenthPair[parenth]:
                    parList.pop()
                else:
                    return False
            
        if len(parList) == 0:
            return True
        return False

