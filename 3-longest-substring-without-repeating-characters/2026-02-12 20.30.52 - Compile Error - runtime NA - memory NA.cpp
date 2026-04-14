#include <set>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> current_chars;
        int l = 0;

        for(int r = 0; r < s.size(); r++)   {
            while(current_chars.count(s[r]))    { //remove all letters that break the condition
                current_chars.erase(s[l]);
                l++;
            }
            current_chars.insert(s[r]);
            max_string = max(max_string, r - l + 1);
        }
        return max_string;
    }
};