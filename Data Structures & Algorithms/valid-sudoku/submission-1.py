class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {index: [] for index in range(9) }
        columns = {index: [] for index in range(9)}
        square = {index: [] for index in range(9)}
        for row in range(9):
            for column in range(9):
                if board[row][column] == ".":
                    pass
                elif board[row][column] != "." and \
                    board[row][column] not in rows[row] and \
                    board[row][column] not in columns[column] and \
                    board[row][column] not in square[(int(row/3) * 3 + int(column/3))]:
                    rows[row].append(board[row][column])
                    columns[column].append(board[row][column])
                    square[(int(row/3) * 3 + int(column/3))].append(board[row][column])
                else:
                    return False
        return True  