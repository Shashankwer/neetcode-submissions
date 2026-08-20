class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        island = 'a'
        ROW = len(grid)
        COL = len(grid[0])
        def dfs(row, col,island, area):
            if row < 0 or col < 0 or row >= ROW or col>=COL:
                return 0
            if grid[row][col] == 1:
                grid[row][col] = island
                area = 1 + dfs(row-1, col, island, area) + dfs(row, col-1, island, area) + dfs(row+1, col, island, area) + dfs(row, col+1, island, area)
                return area
            else:
                return 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col, island, 0))
                    island = chr(ord(island)+1)
        return max_area


        
