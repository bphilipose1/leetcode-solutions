class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0)   {
            return 0;
        }

        int l = 0;
        int r = height.size() - 1;
        int left_max = height[0];
        int right_max = height[height.size()-1];
        int result = 0;

        while(l < r)    {
            if(left_max < right_max)  {
                l += 1;
                left_max = max(left_max, height[l]);
                result += left_max - height[l];
            }
            else    {
                r -= 1;
                right_max = max(right_max, height[r]);
                result += right_max - height[r];
            }
        }
        return result;
        //Time Complexity: O(n)
        //Space Complexity: O(1)
    }
};