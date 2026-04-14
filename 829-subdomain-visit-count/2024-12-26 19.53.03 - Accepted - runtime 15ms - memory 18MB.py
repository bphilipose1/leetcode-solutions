class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitDict = {}
        for entry in cpdomains:
            time, domain = entry.split(' ')
            domainArr = domain.split('.')
            print(domainArr)
            for i in range(len(domainArr)-1, -1, -1):
                print(i)
                level = '.'.join(domainArr[i:])
                print(level)
                if level not in visitDict:
                    visitDict[level] = int(time)
                else:
                    visitDict[level] += int(time)
        print(visitDict)
        resultArr = []
        for domain, freq in visitDict.items():
            tempStr = str(freq) + " " + str(domain)
            print(tempStr)
            resultArr.append(tempStr)
        return resultArr