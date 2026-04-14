from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultList=[]
        dictList = []

        for s in strs:
            found = False
            tempDict = Counter(s)
            for z in range(0, len(dictList)):
                if dictList[z] == tempDict:
                    resultList[z].append(s)
                    found = True
            if found == False:
                dictList.append(tempDict)
                resultList.append([s])
        return resultList
