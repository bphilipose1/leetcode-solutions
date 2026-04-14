class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        
        while l < r and r < len(prices):
            tempProfit = prices[r] - prices[l]
            #if the right price - left price is negative or 0 reset the window.
            if tempProfit <= 0: 
                l = r
                r += 1
            else:
                if tempProfit > maxProfit:
                    maxProfit=tempProfit
                r+=1
        return maxProfit
            