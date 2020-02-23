# 174. Dungeon Game
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        DP.
        dp[r][c] represents the min hp needed at [r, c].
        TODO.
        '''
        d = dungeon
        rows, cols = len(d), len(d[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                need = min(dp[r + 1][c], dp[r][c + 1]) - d[r][c]
                dp[r][c] = 1 if need <= 0 else need
        return dp[0][0]