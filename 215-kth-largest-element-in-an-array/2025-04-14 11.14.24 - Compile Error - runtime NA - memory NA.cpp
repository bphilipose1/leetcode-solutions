class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;


        //O(n)
        for(int num: nums)  {
            minHeap.push(num); //O(logn)
            if (minHeap.size() > k) {
                minHeap.pop()
            }
        }
        return minHeap.top();
    }
};