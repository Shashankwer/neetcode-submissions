class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        next_buy = next_sell = 0
        curr_buy = curr_sell = 0
        for i in range(n-1,-1,-1):
            curr_buy = max(next_buy, -prices[i] + next_sell)
            curr_sell = max(next_sell, prices[i] + next_buy)
            next_buy = curr_buy
            next_sell = curr_sell
        return curr_buy