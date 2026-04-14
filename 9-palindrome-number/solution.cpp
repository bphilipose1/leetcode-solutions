class Solution {
public:
    bool isPalindrome(int x) {
        string parseString = std::to_string(x);
        for(int i = 0; i <= parseString.length()/2; ++i)  {
            if(parseString[i]!=parseString[parseString.length() - i - 1])   {
                return false;
            }
        }
        return true;
    }
};