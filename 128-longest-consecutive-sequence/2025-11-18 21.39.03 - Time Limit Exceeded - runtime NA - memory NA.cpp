#include <algorithm>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> sequence_set(nums.begin(), nums.end());
        int longest = 0;
        for(int num: nums)  {
            if(!sequence_set.count(num - 1)) { //if this isnt a non starting point for a sequence
                int length = 1;
                int cur = num;
                while (sequence_set.count(cur + 1)) {
                    cur++;
                    length++;
                }

                longest = max(longest, length);
            }
        }
        
        return longest;
    }

    //time complexity: O(n)
    //Space Complexity: O(n)
};