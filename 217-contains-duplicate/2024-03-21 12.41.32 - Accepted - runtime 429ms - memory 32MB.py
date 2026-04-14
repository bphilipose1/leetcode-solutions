class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for x in nums:
            if x in hashSet:
                return True
            else:
                hashSet.add(x)
        return False
        