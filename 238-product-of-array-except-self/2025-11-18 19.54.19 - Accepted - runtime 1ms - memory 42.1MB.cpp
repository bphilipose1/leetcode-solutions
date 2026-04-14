class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
        - Perhaps we can use a prefix (product before) and suffix (product after)
            1. Do two passes, one to make prefix array and another for the suffix product array, each cell is product not inclusive of value at index, and product of all before or all after that index
            2. then do final pass and calculate answer.

            1, 2, 3, 4
        pre:1, 1, 2, 6
        suf:1, 1, 1, 1
        24, 8, 12, 6
        */
        int N = nums.size();
        vector<int> answer(N);
        vector<int> prefix_prod(N,1);
        vector<int> suffix_prod(N,1);
        int prefix_idx;
        int suffix_idx;
        for(int i = 1; i < nums.size(); i++)    {
            //get the prefix
            prefix_idx = i;
            prefix_prod[prefix_idx] = prefix_prod[prefix_idx - 1] * nums[prefix_idx - 1]; 

            suffix_idx = nums.size() - 1 - i;
            suffix_prod[suffix_idx] = suffix_prod[suffix_idx + 1] * nums[suffix_idx + 1]; 
                  
        }

        for(int i = 0; i < nums.size(); i++)    {
            answer[i] = prefix_prod[i] * suffix_prod[i];
        }

        return answer;
        //Time Complexity: O(n)
        //Space Complexity: O(n)
        
    }
};