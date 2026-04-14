class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        vector<int> path;
        vector<vector<int>> ans;
        recursiveBacktrack(nums, 0, path, ans);
        return ans;
    }

    void recursiveBacktrack(vector<int>& nums, int startIndex, vector<int> path, vector<vector<int>>& ans) {
        ans.push_back(path); 
        
        for (int i = startIndex; i < nums.size(); ++i) {
            if (i > startIndex && nums[i] == nums[i-1]) // 1 2 3 [3 4]
                continue; 
            
            path.push_back(nums[i]);
            recursiveBacktrack(nums, i + 1, path, ans);
            path.pop_back(); 
        }
    }
};
