class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(h, (distance, point))
        results = []
        for _ in range(k):
            distance, min_point = heapq.heappop(h)
            results.append(min_point)
        return results