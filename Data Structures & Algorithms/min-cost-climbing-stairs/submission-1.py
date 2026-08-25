class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_copy = [-1] * (len(cost))
        cost_len = len(cost)
        for n in range(len(cost)-1, -1, -1):
            if n == (len(cost)-1) or n == (len(cost)-2):
                cost_copy[n] = cost[n]
            else:
                
                cost_copy[n] = min(cost[n]+cost_copy[n+1], cost[n]+cost_copy[n+2])
        return min(cost_copy[0],cost_copy[1])