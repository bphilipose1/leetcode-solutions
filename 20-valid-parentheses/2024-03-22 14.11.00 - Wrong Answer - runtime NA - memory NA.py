class Solution:
    def isValid(self, s: str) -> bool:
        parenthStack = []
        parDict = {')' :'(', '}': '{', ']':'['}
        for parenthesis in s:
            if parenthesis in parDict:
                if parenthStack and parDict[parenthesis] == parenthStack[-1]:
                    parenthStack.pop()
            else:
                parenthStack.append(parenthesis)
        if len(parenthStack) == 0:
            return True
        return False
        