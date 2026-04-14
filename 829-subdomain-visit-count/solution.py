class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitDict = {}
        for entry in cpdomains:
            time, domain = entry.split(' ')
            domainArr = domain.split('.')
            for i in range(len(domainArr)-1, -1, -1):
                level = '.'.join(domainArr[i:])
                if level not in visitDict:
                    visitDict[level] = int(time)
                else:
                    visitDict[level] += int(time)

        resultArr = []
        for domain, freq in visitDict.items():
            tempStr = str(freq) + " " + str(domain)
            resultArr.append(tempStr)
        return resultArr