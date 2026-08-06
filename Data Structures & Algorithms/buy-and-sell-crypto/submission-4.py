class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = prices[0] 
        for price in prices  :
            profit = price - min_prices 
            max_profit = max(profit,max_profit)
            min_prices = min(min_prices , price )
        return max_profit 

