class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        perm = []
        def isPalindrome(s, left, right):
            
            while right > left: #finish comparisons
                if s[right] != s[left]: #comparisons are not palindrome
                    return False
                right -= 1
                left += 1
            return True

        def recFunc(i):
            if i >= len(s):
                result.append(perm.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    perm.append(s[i:j + 1])
                    recFunc(j + 1)
                    perm.pop()
            
        recFunc(0)

        return result