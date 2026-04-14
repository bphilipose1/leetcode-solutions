
class Solution {
public:
    bool isPalindrome(string s) {
        int l_ptr = 0;
        int r_ptr = s.size() - 1;
        
        while(l_ptr < r_ptr)    {
            while (l_ptr < r_ptr && !isalphaNum(s[l_ptr])) {
                l_ptr += 1;
            }
            while (r_ptr > l_ptr && !isalphaNum(s[r_ptr])) {
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

    bool isalphaNum(char c)    {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
    //Time Complexity: O(n)
    //Space Complexity: O(1)
};