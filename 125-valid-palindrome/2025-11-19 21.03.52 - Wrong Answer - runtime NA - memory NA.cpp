
class Solution {
public:
    bool isPalindrome(string s) {
        int l_ptr = 0;
        int r_ptr = s.size() - 1;
        
        while(l_ptr < r_ptr)    {
            while (l_ptr < r_ptr && !isalpha(s[l_ptr])) {
                l_ptr += 1;
            }
            while (r_ptr > l_ptr && !isalpha(s[r_ptr])) {
                r_ptr -= 1;
            }
            if(tolower(s[l_ptr]) != tolower(s[r_ptr]))    {
                return false;
            }
            l_ptr++;
            r_ptr--;
        }
        return true;
    }
};