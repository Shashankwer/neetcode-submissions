class Solution:
    def manhattandist(self, p1, p2):
        return abs(p2[0]-p1[0]) + abs(p1[1]-p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        adj_matrix = {i: [] for i in range(num_points)}
        for i in range(num_points):
            temp = [0]*num_points
            for j in range(i+1, num_points):
                heapq.heappush(adj_matrix[i], (self.manhattandist(points[i], points[j]), j))
                heapq.heappush(adj_matrix[j], (self.manhattandist(points[i], points[j]), i))
        minHeap = [[0,0]]
        visit = set()
        res = 0
        while len(visit)<num_points:
            cost, index = heapq.heappop(minHeap)
            if index in visit:
                continue
            res += cost
            visit.add(index)
            for nCost,nIndex in adj_matrix[index]:
                if nIndex not in visit:
                    heapq.heappush(minHeap, [nCost, nIndex])
        return res