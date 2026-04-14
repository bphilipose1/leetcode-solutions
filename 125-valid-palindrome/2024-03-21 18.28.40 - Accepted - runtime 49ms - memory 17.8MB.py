class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedString = ''.join(char for char in s.lower() if char.isalnum())
        return cleanedString == cleanedString[::-1]