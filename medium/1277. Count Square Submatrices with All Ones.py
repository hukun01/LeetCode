# 1277. Count Square Submatrices with All Ones
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        '''
        DP with careful observation.

        If A[r][c] == 0, no square;
        If A[r][c] == 1, we have a new square with side 1, and we
        also have another (k-1) squares that can be formed using A[r][c],
        where k is the side.
        In general, with A[r][c] == 1, if the square side is k, the number
        of new squares that cover A[r][c] is k.
        '''
        A = matrix
        rows, cols = len(A), len(A[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if A[r][c] > 0 and r > 0 and c > 0:
                    A[r][c] = min(A[r - 1][c], A[r][c - 1], A[r - 1][c - 1]) + 1
                ans += A[r][c]
        return ans