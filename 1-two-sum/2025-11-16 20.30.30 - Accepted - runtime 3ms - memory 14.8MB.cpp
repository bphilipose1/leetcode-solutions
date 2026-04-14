#include <map>
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    /*
    - Sort
        Time Complexity:  O(nlog(n))
        Space Compelxity: O(1)
    - Store and match in a Data structure
        - Hashmap? 
            Time Complexity: O(n)
            Space Complexity: O(n)
    */
    std::unordered_map<int, int> indices;
    indices[nums[0]] = 0;

    for(int idx = 1; idx < nums.size(); idx ++)  {
        int find_val = target - nums[idx];
        if(indices.count(find_val) && indices[find_val] != idx) {
            return {idx, indices[find_val]};
        }

        indices[nums[idx]] = idx;
        
    }
    return {0,0};

    }
};