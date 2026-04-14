#include <unordered_map>
#include <queue>
#include <vector>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //store frequency counts (O(n))
        unordered_map<int, int> freq;
        for (int n: nums) freq[n]++;

        //like normal do the top k elements
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;

        for(auto& pair:freq)    {
            minHeap.push({pair.second, pair.first});
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        vector<int> result;
        while(!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return result;
    }
};