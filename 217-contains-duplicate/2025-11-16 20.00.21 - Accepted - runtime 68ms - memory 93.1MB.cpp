#include <algorithm>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        /*We want to find duplicates
        Options:
        - Sort 
            Time Complexity: O(nLog(n)) 
            Space Complextiy: O(1)
        - Parse Array
            Time Complexity: O(n^2) 
            Space Complextiy: O(1)
        - Data structure to remove dups (we choose this one)
            Time Complexity: O(n) 
            Space Complextiy: O(n) 

        */
        return std::unordered_set(nums.begin(), nums.end()).size() < nums.size();
    }
};