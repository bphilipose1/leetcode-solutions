#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        /*
        Possible Solutions:
        - Get Frequency of letter arrays, for each word and compare them. 
            Time Complexity: O(n*m) m is number of strings, n is max letters in one word
            Space Complexity: O(m)
        Steps:
            1. Go through each word and count letter frequency O(n * m), O(1)
            2. Store the Arrays in a dict, and use their unique letter freq arrays as keys. (O(m)), O(m)
            3. then go through the hashmap and group to make the final list (O(m))



        - Sort each word's letter then sort each word, then go through the list and group 
            Time Complexity: (nlogn * nlogn + n) = O(n^2(logn)^2)
            Space Complexity: O(1)
        */

        //1. Go through each word and count letter frequency O(n * m), O(1)
        unordered_map<string, vector<string>> anagram_dict;
        int letter_idx;
        for(string str: strs)   {
            vector<int> letter_arr(26, 0);
            for(int letter: str)    {
                letter_idx = letter - 'a';
                letter_arr[letter_idx] += 1;
            }
            //2. Store the Arrays in a dict, and use their unique letter freq arrays as keys. (O(m)), O(m)
            string key = to_string(letter_arr[0]);
            for(int i = 1; i < 26; i++) {
                key += "," + to_string(letter_arr[i]);
            }

            anagram_dict[key].push_back(str);
        }

        //3. then go through the hashmap and group to make the final list (O(m))
        vector<vector<string>> values;
        for(pair<const string, const vector<string>> pair: anagram_dict)  {
            values.push_back(pair.second);
        }
        return values;

    }
};