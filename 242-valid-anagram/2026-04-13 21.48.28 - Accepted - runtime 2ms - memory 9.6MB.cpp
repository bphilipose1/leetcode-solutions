class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size())    { //Check if the sizes are not same, instant red flag for not being anagram
            return false;
        }
        //We need to get the number of letters and that can tell us if its an anagram
        //Approach 1, sort the letters O(nlogn), and do a linear check O(n) = (O(nlogn)) time and O(1) space
        //Approach 2, store the letters time: O(1), space actually O(1) since most different letters is 26, and do a linear check O(n) time = O(n) time
            
            
            
        //Step 1 create 26 cell array of letters
        int let_count[26]{};
        int let_index = 0;
        int idx = 0;
        //Step 2, sweep s string and store letter counts
        for(int let = 0; let < s.size(); let++) {
            let_index = tolower(s[let]) - 'a';
            let_count[let_index] += 1;
        }

        //Step 3, sweep t string and either store its letter counts, or we can deduct from s array, and if any letter is - count then we know its wrong, saves us from extra array and final linear pass.
        for(int j = 0; j < t.size(); j++) {
            idx = tolower(t[j]) - 'a';
            let_count[idx] -= 1;
            if(let_count[idx] < 0)    {
                return false;
            }
        }
        return true;

    
    }
};

/*
OMEGA OPTIMAL SOLUTION:
bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;

    int let_count[26]{};

    for (char c : s) let_count[tolower(c) - 'a']++;
    for (char c : t) {
        if (--let_count[tolower(c) - 'a'] < 0) return false;
    }

    return true;
}
*/