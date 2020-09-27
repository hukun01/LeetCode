class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        '''
        DP.
        Similar to 152. Maximum Product Subarray.
        One trap is that `math.inf * 0` = `nan`, so we need to leave the
        multiplication outside the comparison.
        '''
        R, C = len(grid), len(grid[0])
        f = [[[0, 0] for c in range(C+1)] for r in range(R+1)] # [max, min]
        for r in range(len(f)):
            f[r][0] = [-math.inf, math.inf]
        for c in range(len(f[0])):
            f[0][c] = [-math.inf, math.inf]
        f[1][0] = [1, 1]
        f[0][1] = [1, 1]
        for r in range(R):
            for c in range(C):
                if (val := grid[r][c]) < 0:
                    f[r+1][c+1][0] = min(f[r+1][c][1], f[r][c+1][1]) * val
                    f[r+1][c+1][1] = max(f[r+1][c][0], f[r][c+1][0]) * val
                else:
                    f[r+1][c+1][0] = max(f[r+1][c][0], f[r][c+1][0]) * val
                    f[r+1][c+1][1] = min(f[r+1][c][1], f[r][c+1][1]) * val
        MOD = 10 ** 9 + 7
        return f[R][C][0] % MOD if f[R][C][0] >= 0 else -1