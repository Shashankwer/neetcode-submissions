class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.board = [["."]*n for i in range(n)]
        def backtrack(r):
            if r == n:
                row_copy = ["".join(row) for row in self.board]
                res.append(row_copy)
                return 
            for c in range(n):
                if self.isSafe(r, c):
                    self.board[r][c] = "Q"
                    backtrack(r+1)
                    self.board[r][c] = "."
        backtrack(0)
        self.board = None
        return res
    
    def isSafe(self, r, c):
        row = r - 1
        while row >= 0:
            if self.board[row][c] == "Q":
                return False
            row -=1
        column = c - 1
        while column > 0:
            if self.board[r][column] == "Q":
                return False
            column -= 1
        row = r-1
        column = c - 1
        while row >= 0 and column >= 0:
            if self.board[row][column] == "Q":
                return False
            row -= 1
            column -= 1
        row = r - 1
        column = c + 1
        while row >= 0 and column < len(self.board):
            if self.board[row][column] == "Q":
                return False
            row -= 1
            column += 1
        return True
            