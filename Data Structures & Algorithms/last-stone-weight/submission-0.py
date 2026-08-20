class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)
        while len(h) > 1:
            first = heapq.heappop(h)
            second = heapq.heappop(h)
            if second > first:
                heapq.heappush(h, first - second)
        h.append(0)
        return abs(h[0])
        
