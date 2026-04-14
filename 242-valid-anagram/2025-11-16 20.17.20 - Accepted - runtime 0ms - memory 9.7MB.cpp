#include <algorithm>
class Solution {
public:
    bool isAnagram(string s, string t) {
        /*
        We need to see if the same frequency of letters are in both words
        - Use a Dictionary to track letter frequency (better)
            Time Complexity: O(n + n) = O(n)
            Space Complexity: O(1) <- it is only max size of 26, since only 26 letters. So we can use a list.
        - Sort the letters then parse through 
            Time Complexity: O(n + nlog(n)) = O(nlog(n))
            Space Complexity: O(n)
        */

        //Check if the sizes are the same.
        if (s.size() != t.size())   {
            return false;
        }
        vector<int> letter_count(26, 0);
        //This gets the letter frequency of s
        for(int i = 0; i < s.size(); i++)   {
            int letter_idx = s[i] - 'a';
            letter_count[letter_idx] += 1;
        }

        //Repeat what we did with s, but remove if its in t
        for(int i = 0; i < t.size(); i++)   {
            int letter_idx = t[i] - 'a';
            letter_count[letter_idx] -= 1;
        }

        //then check if the array is all 0s.

        for(int val: letter_count)   {
            if (val != 0)
                return false;
        }
        return true;
    }
};