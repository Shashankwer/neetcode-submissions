class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = -1
        profit = 0
        for price in prices:
            profit = max(price-buy, profit)
            buy = min(price, buy)
        return profit
