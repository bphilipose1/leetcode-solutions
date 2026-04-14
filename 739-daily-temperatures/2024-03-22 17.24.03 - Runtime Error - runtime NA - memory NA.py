class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultArr = [0] * len(temperatures)
        minStack = []
        for x in range(len(temperatures)):
            if temperatures[x] > temperatures[minStack[-1]] and minStack:
                while minStack:
                    if temperatures[x] > temperatures[minStack[-1]]:
                        resultArr[minStack[-1]] = x-minStack[-1]
                        minStack.pop()
                    else:
                        break
            minStack.append(x)

        return resultArr

                    
        
