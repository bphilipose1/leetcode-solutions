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
                qp.heappush(temp, y-x)
        
        if temp:
            return -temp[0]
        else:
            return 0
        return temp