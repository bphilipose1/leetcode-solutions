class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                temp = prices[sell] - prices[buy]
                if temp > maxProfit:
                    maxProfit = temp

        return maxProfit





        