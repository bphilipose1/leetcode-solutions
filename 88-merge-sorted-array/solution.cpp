class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int num1it = m-1;
        int num2it = n-1;
        int startResult = n+m-1;
        while(num1it >= 0 && num2it >= 0)  {
            if(nums1[num1it] >= nums2[num2it])  {
                nums1[startResult--] = nums1[num1it--];
            }
            else    {
                nums1[startResult--] = nums2[num2it--];
            }
        }
        while(num2it >= 0) {
            nums1[startResult--] = nums2[num2it--];
        }
        while(num1it >= 0) {
            nums1[startResult--] = nums1[num1it--];
        }
        
    }
};