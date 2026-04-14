from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultList = defaultdict(list)

        for s in strs:
            tempKey = tuple(sorted(s))
            resultList[tempKey].append(s)

        return resultList.values()