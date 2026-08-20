class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # dikstra's algorithm
        N = len(grid)
        minHeap = [(grid[0][0],0,0)]
        dest = float("inf")
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        visit = set()
        visit.add((0,0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc  in directions:
                neighR, neighC = r+dr, c+dc
                if (neighR < 0 or neighC < 0 or neighR == N or neighC == N or (neighR, neighC) in visit):
                    continue
                visit.add((neighR, neighC))
                heapq.heappush(minHeap, [max(t, grid[neighR][neighC]), neighR, neighC])

