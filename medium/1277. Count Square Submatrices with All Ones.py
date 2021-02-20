# 1277. Count Square Submatrices with All Ones
class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        '''
        DP with careful observation.

        If A[r][c] == 0, no square;
        If A[r][c] == 1, we have a new square with side 1, and we
        also have another (k-1) squares that can be formed using A[r][c],
        where k is the side.
        In general, with A[r][c] == 1, if the square side is k, the number
        of new squares that cover A[r][c] is k.

        Let f[r][c] be the max side length for the square whose bottom right
        is at (r, c). The max side square length is determined by the smallest
        neighbor squares.
        f[r][c] = min(f[r - 1][c], f[r][c - 1], f[r - 1][c - 1]) + 1

        Time: O(R C)
        Space: O(R C)
        '''
        R, C = len(A), len(A[0])
        f = [[0] * C for _ in range(R)]
        ans = 0
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    f[r][c] = min(f[r - 1][c], f[r][c - 1], f[r - 1][c - 1]) + 1
                ans += f[r][c]
        return ans