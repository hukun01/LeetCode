# 304. Range Sum Query 2D - Immutable
class NumMatrix:
    '''
    Prefix sums 2d.
    '''
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        R, C = len(matrix), len(matrix[0])
        self.pre = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.pre[r+1][c+1] = matrix[r][c] + self.pre[r][c+1] + \
                    self.pre[r+1][c] - self.pre[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.pre:
            return 0
        return self.pre[row2 + 1][col2 + 1] - self.pre[row1][col2 + 1] - \
            self.pre[row2 + 1][col1] + self.pre[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)