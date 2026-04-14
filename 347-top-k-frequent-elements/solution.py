from collections import Counter
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        
        def getItem(key):  
            return freqDict[key]
        
        result = sorted(freqDict.keys(), key=getItem, reverse = True)
        return result[0:k]