#include <algorithm>
#include <vector>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int tot_size = nums.size();
        int val;
        int cur_val;
        for(int i = 0; i < tot_size; i++) {
            if(i > 0 && nums[i] == nums[i - 1]) continue; //we already tried this
            if(nums[i] > 0) break; //no possible combos with only pos nums left
            cur_val = nums[i];
            ///do two sum in this, from range i -> nums.size();
            int l = i + 1;
            int r = tot_size-1;
            int temp_val;
            while(l < r)    {
                temp_val = nums[r] + nums[l] + cur_val;
                if(temp_val < 0)    {
                    l++;
                }
                else if(temp_val > 0)   {
                    r--;
                }
                else    {
                    result.push_back({cur_val, nums[l], nums[r]});
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l-1])    {
                        l++;
                    }
                }
            }
        }
        return result;
    }
};