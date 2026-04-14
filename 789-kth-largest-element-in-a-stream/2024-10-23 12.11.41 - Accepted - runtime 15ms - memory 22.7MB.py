class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.top_k = k
        heapq.heapify(self.minHeap) #creates it into a min heap
        while len(self.minHeap) > self.top_k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #add to minheap
        heapq.heappush(self.minHeap, val)
        #pop from minheap to see top k score from the top of heap
        if len(self.minHeap) > self.top_k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)