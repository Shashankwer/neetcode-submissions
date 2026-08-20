class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        MAX_INF = 2**31-1
        MAX_ROW, MAX_COL = len(grid), len(grid[0])
        visit = set()
        q = deque()
        def addCell(r, c):
            if (min(r, c) < 0 or r == MAX_ROW or c == MAX_COL or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(MAX_ROW):
            for c in range(MAX_COL):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c-1)
                addCell(r, c+1)
            dist+=1
        
        
            
