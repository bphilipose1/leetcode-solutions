class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() < 2)   {
            return 0;
        }
        int l = 0;
        int r = 1;
        int temp_profit = 0;
        int max_profit = 0;
        while(r < prices.size())    {
            temp_profit = prices[r] - prices[l];
            if (temp_profit <= 0)  { //our reset condition
                l = r;
            }
            else    {
                max_profit = (temp_profit > max_profit) ? temp_profit : max_profit;
            }
            r += 1;

        }
        return max_profit;
    }
    //Time Complexity: O(n)
    //Space Complexity: O(1)
};