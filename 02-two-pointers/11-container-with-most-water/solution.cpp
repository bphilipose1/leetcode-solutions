class Solution {
public:
    int maxArea(vector<int>& height) {
        /*
        we need to maximize two things, the outter bar height, and the outter bar widths
            - We can start with the absolute best bar width and slowly decrease if needed to find the best bar heights
        */
        int l = 0;
        int r = height.size() - 1;
        int max_water = 0;

        int temp_width = 0;
        int temp_height = 0;
        int temp_water_amount = 0;
        while (l < r)   {
            //calculate current water amount
            temp_width = r - l;
            temp_height = min(height[r], height[l]);
            temp_water_amount = temp_width * temp_height;
            

            //check if this water amount is the best so far
            if (temp_water_amount > max_water)  {
                max_water = temp_water_amount;
            }

            //pick next best move (greedy)
            (height[l] > height[r]) ? r-- : l++;
        }
        return max_water;
    }
    //Time Complexity: O(n)
    //Space Complexity: O(1)
};