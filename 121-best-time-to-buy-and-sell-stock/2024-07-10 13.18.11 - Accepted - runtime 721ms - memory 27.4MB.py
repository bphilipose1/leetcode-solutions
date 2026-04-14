class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        sell, buy = 1, 0
        
        while sell < len(prices):
            temp = prices[sell] - prices[buy]
            if temp <= 0:
                buy = sell
            if temp > maxProfit:
                maxProfit = temp
            sell += 1 
        return maxProfit





        