class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultArr = [0] * len(temperatures)
        for x in range(len(temperatures)):
            for z in range(x, len(temperatures)):
                if temperatures[x] < temperatures[z]:
                    resultArr[x] = z-x
                    break
        return resultArr
