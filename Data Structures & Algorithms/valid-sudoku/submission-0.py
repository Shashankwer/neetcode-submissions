class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {i:[] for i in range(9)}
        column_map = {i:[] for i in range(9)}
        square_map = {i:[] for i in range(9)}
        for row_index in range(9):
            for column_index in range(9):
                if board[row_index][column_index] == '.':
                    pass
                else:
                    if board[row_index][column_index] in row_map[row_index]:
                        return False
                    elif board[row_index][column_index] in column_map[column_index]:
                        return False
                    elif board[row_index][column_index] in square_map[(row_index//3)*3+(column_index//3)]:
                        return False
                    else:
                        row_map[row_index].append(board[row_index][column_index])
                        column_map[column_index].append(board[row_index][column_index])
                        square_map[(row_index//3)*3+(column_index//3)].append(board[row_index][column_index])
        return True