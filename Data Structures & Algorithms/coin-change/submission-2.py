class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def dfs(a):
            if a in dp:
                return dp[a]
            if a < 0:
                return -1
            res = 1e9
            for c in range(len(coins)-1,-1,-1):
                if a - coins[c] >=0:
                    res = min(res, 1+dfs(a-coins[c]))
            dp[a] = res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins == 1e9 else minCoins