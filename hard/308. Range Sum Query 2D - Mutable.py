# 308. Range Sum Query 2D - Mutable
class NumMatrix:
    '''
    Fenwick tree, Binary Indexed Tree (BIT), 2d version.

    Similar to 307. Range Sum Query - Mutable
    '''

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        R, C = len(matrix), len(matrix[0])
        self.bit = BinaryIndexedTree2D(R, C)
        for r in range(R):
            for c in range(C):
                self.bit.update(r + 1, c + 1, matrix[r][c])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.sumRegion(row, col, row, col)
        self.bit.update(row + 1, col + 1, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return \
            self.bit.query(row2 + 1, col2 + 1) - \
            self.bit.query(row2 + 1, col1) - \
            self.bit.query(row1, col2 + 1) + \
            self.bit.query(row1, col1)

class BinaryIndexedTree2D:

    def __init__(self, r, c):
        self.data = [[0] * (c + 1) for _ in range(r + 1)]
        self.R = r + 1
        self.C = c + 1

    def low_bit(self, i):
        '''
        Isolate the last bit from i.
        '''
        return i & (-i)
    
    def update(self, r, c, v):
        while r < self.R:
            self.update_c(r, c, v)
            r += self.low_bit(r)
            
    def update_c(self, r, c, v):
        while c < self.C:
            self.data[r][c] += v
            c += self.low_bit(c)
    
    def query(self, r, c):
        ans = 0
        while 0 < r:
            ans += self.query_c(r, c)
            r -= self.low_bit(r)
        return ans
    
    def query_c(self, r, c):
        ans = 0
        while 0 < c:
            ans += self.data[r][c]
            c -= self.low_bit(c)
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)