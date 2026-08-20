class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        def dfs(row, col):
            if min(row, col) < 0 or row >= ROW or col >= COL or board[row][col] != "O":
                return
            if board[row][col] == "O":
                board[row][col] = "~"
                dfs(row-1, col)
                dfs(row+1, col)
                dfs(row, col-1)
                dfs(row, col+1)
        for row in [0, ROW-1]:
            for col in range(COL):
                if board[row][col] == "O":
                    dfs(row,col)
        for col in [0, COL-1]:
            for row in range(ROW):
                if board[row][col] == "O":
                    dfs(row,col)
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "~":
                    board[row][col] = "O"