class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;


        //O(n)
        for(int num: nums)  {
            maxHeap.push(num); //O(logn)
            if (maxHeap.size() > k) {
                maxHeap.pop()
            }
        }
        return maxHeap.top();
    }
};