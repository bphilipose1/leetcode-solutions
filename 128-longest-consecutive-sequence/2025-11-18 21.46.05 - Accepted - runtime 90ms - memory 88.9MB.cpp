#include <algorithm>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> sequence_set(nums.begin(), nums.end());
        int longest = 0;

        for (int num : sequence_set) {
            // if this is the start of a sequence
            if (!sequence_set.count(num - 1)) {
                int length = 1;
                while (sequence_set.count(num + length)) {
                    length++;
                }

                longest = max(longest, length);
            }
        }

        return longest;
    }

    // Time complexity: O(n)
    // Space complexity: O(n)
};