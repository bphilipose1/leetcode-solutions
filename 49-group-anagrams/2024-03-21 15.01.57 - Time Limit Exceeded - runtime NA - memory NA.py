from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultList=[]
        dictList = []

        for s in strs:

            tempDict = Counter(s)
            if tempDict in dictList:
                for z in range(0, len(dictList)):
                    if dictList[z] == tempDict:
                        resultList[z].append(s)

            else:
                dictList.append(tempDict)
                resultList.append([s])
        return resultList
