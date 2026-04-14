class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hq
        hq.heapify(nums)
        for i in range(len(nums) - k + 1):
            result = hq.heappop(nums)
        return result