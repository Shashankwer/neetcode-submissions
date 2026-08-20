class Solution:
    def mark_island(self, i,j, island=0):
        if i < 0 or j < 0 or i >= self.rows or j>=self.columns:
            return
        if self.grid[i][j] == "0":
            return
        if self.grid[i][j] == "1":
            self.grid[i][j] = island
            # mark all of them
            self.mark_island(i+1,j, island)
            self.mark_island(i,j+1, island)
            self.mark_island(i-1,j, island)
            self.mark_island(i,j-1, island)
        else:
            return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])
        curr_island = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == "1":
                    curr_island+=1
                    self.mark_island(i,j, curr_island)
        #print(self.grid)
        return curr_island
                        
                    
                    