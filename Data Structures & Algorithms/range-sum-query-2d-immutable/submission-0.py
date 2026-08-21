class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # prefix sum matrix
        row, columns = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(columns)] for _ in range(row)]
        
        for r in range(row):
            self.matrix[r][0] = matrix[r][0]
            for c in range(1,columns):
                self.matrix[r][c] = self.matrix[r][c-1] + matrix[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        
        for r in range(row1, row2+1):
            if col1 > 0:
                result += self.matrix[r][col2] - self.matrix[r][col1-1]
            else:
                result += self.matrix[r][col2]
        return result


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)