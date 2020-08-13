# 308. Range Sum Query 2D - Mutable
low_bit = lambda x: x & (-x)

class NumMatrix:
    '''
    Fenwick tree, Binary Indexed Tree (BIT).

    Similar to 307. Range Sum Query - Mutable
    '''

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        R, C = len(matrix), len(matrix[0])
        self.tree = [[0] * (C + 1) for _ in range(R+1)]
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                '''
                # Simpler update, but slower as O(logN).
                self.update(r-1, c-1, matrix[r-1][c-1])
                '''
                # O(1) update
                self.tree[r][c] += matrix[r-1][c-1]
                if (parent_row := r + low_bit(r)) <= R:
                    self.tree[parent_row][c] += self.tree[r][c]
                if (parent_col := c + low_bit(c)) <= C:
                    self.tree[r][parent_col] += self.tree[r][c]
                if parent_row <= R and parent_col <= C:
                    self.tree[parent_row][parent_col] -= self.tree[r][c]

    def update(self, row: int, col: int, val: int) -> None:
        dif = val - self.sumRegion(row, col, row, col)
        row += 1
        col += 1
        while row < len(self.tree):
            y1 = col
            while y1 < len(self.tree[0]):
                self.tree[row][y1] += dif
                y1 += low_bit(y1)
            row += low_bit(row)

    @staticmethod
    def query(tree, row, col):
        ans = 0
        row += 1
        col += 1
        while row >= 1:
            y1 = col
            while y1 >= 1:
                ans += tree[row][y1]
                y1 -= low_bit(y1)
            row -= low_bit(row)
        return ans

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return \
    NumMatrix.query(self.tree, row2, col2) + \
    NumMatrix.query(self.tree, row1-1, col1-1) - \
    NumMatrix.query(self.tree, row2, col1-1) - \
    NumMatrix.query(self.tree, row1-1, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)