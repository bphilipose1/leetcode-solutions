#include <unordered_map>
#include <queue>
#include <vector>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /*
        Solutions: 
        1. Get the freq dict
        2. 
        */


        //store frequency counts (O(n))
        unordered_map<int, int> freq;
        for (int n: nums) freq[n]++;

        vector<vector<int>> freq_nums(nums.size() + 1);
        //have a vector store freq, and nums that have that freq
        for(const auto& pair : freq)    {
            freq_nums[pair.second].push_back(pair.first);
        }
        vector<int> result;
        for(int i = nums.size(); i > 0; i--)    {
            for(int num : freq_nums[i]) {
                if(result.size() == k)  {
                    return result;
                }
                result.push_back(num);
            }
        }
        return result;

        //Time Complexity: (n + n + n) = O(n)
        //Space Complexity: (n + n) = O(n)


    }
};