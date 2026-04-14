class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq as qp
        temp = [-num for num in stones]
        qp.heapify(temp)
        while len(temp) > 1:
            y = qp.heappop(temp)
            x = qp.heappop(temp)
            if x == y:
                continue
            elif x != y:
                x = -1*((-1*y) - (-1*x))
                qp.heappush(temp, x)
        
        if temp:
            return -temp[0]
        else:
            return 0
        return temp