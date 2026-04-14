from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        result = sorted(freqDict.keys(), key=lambda item: freqDict[item], reverse = True)
        return result[0:k]