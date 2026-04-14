class Solution {
public:
    int search(vector<int>& nums, int target) {
        int r = nums.size() - 1;
        int l = 0;
        int mid;
        while(l<=r) {
            mid = (r + l) / 2;
            if(nums[mid] == target) {
                return mid;
            }
            
            //left sorted portion
            if(nums[l] <= nums[mid])    {
                if(target > nums[mid] || target < nums[l])  {
                    l = mid + 1;
                }    
                else    {
                    r = mid - 1;
                }
            }
            else    {
                if(target < nums[mid] || target > nums[r])  {
                    r = mid - 1;
                }
                else    {
                    l = mid + 1;
                }
            }
        }
        return -1;
    }
};