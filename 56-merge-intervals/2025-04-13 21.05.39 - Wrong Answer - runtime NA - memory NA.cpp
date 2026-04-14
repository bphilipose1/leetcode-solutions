
#include <vector>
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result = {intervals[0]};
        int i = 1;
        while(i < intervals.size())    {
            //check if result[-1] and intervals[i] are overlapping
            vector<int>& last = result.back();
            vector<int> first = intervals[i];

            //if true then pop result, and increment i then result.push_back(new interval)
            if (last[1] >= first[0])    {
                last[1] = max(last[1], first[1]);
                last[0] = min(last[0], first[0]);
            }
            else    {//else result.push_back(intervals[i]) and i ++
                result.push_back(first);
            }
            i++;
        }
        return result;
    }
};