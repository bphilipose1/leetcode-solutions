#include <set>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0;

        int max_string = 0;
        std::set<std::string> current_chars;
        std::string temp_char;
        bool doub_hit = false;
        while(l <= r && r < s.size())    {
            temp_char = s[r];
            doub_hit = current_chars.count(temp_char);
            if (doub_hit == true) { //our reset condition
                if ((r-l) > max_string) {max_string=(r-l);} 
                l = r;
            }
            else    {
                current_chars.insert(temp_char);
            }
            r+=1;
        }
        return max_string;
    }
};