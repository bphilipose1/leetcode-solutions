class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        vector<int> path;
        vector<vector<int>> ans;
        recursiveBacktrack(nums, 0, path, ans);
        return ans;
    }

    void recursiveBacktrack(vector<int>& inputNums, int startIndex, vector<int> path, vector<vector<int>>& ans)    {
        if(startIndex >= inputNums.size())  {
            for(int x = 0; x < ans.size(); x++) {
               if(ans[x] == path)   {
                return;
               } 
            }
            ans.push_back(path);
            return;
        }

        
        //Exclude startIndex
        recursiveBacktrack(inputNums, ++startIndex, path, ans);
        
        //Include startindex
        
        recursiveBacktrack(inputNums, ++startIndex, path.push_back(inputNums[startIndex]), ans)

    }
}
