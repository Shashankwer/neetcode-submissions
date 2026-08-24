class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate, max_rate = 1, max(piles)
        res = max_rate
        mid_rate = (max_rate+min_rate)//2
        while min_rate <= max_rate:
            mid_rate = (max_rate+min_rate)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/mid_rate)
            if totalTime <= h:
                res = mid_rate
                max_rate = mid_rate -1
            else:
                min_rate = mid_rate + 1
        return res