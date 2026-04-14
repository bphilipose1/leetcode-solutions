class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', }
        result = []
        def recBuild(cur, idx):
            if idx == len(digits): #if built string is complete add to result
                result.append(cur[:])
                return
            for char in digit_to_char[digits[idx]]:
                recBuild(cur + char, idx + 1)
        
        recBuild("", 0)
        return result

        