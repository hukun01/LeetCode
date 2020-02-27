# 576. Out of Boundary Paths
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        '''
        dp[r][c][n] means the number of paths out of boundary,
        at (r, c) with n moves left.
        '''
        dp = [[[-1] * (N + 1) for c in range(n)] for r in range(m)]
        def dfs(r, c, steps):
            if not 0 <= r < m or not 0 <= c < n:
                return 1
            if steps == 0:
                dp[r][c][steps] = 0
            if dp[r][c][steps] != -1:
                return dp[r][c][steps]
            dp[r][c][steps] = 0
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dp[r][c][steps] += dfs(r + dr, c + dc, steps - 1)
            return dp[r][c][steps]
        dfs(i, j, N)
        MOD = 10 ** 9 + 7
        return dp[i][j][N] % MOD