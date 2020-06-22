# 174. Dungeon Game
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        '''
        DP.
        dp[r][c] represents the min hp needed at [r, c].
        dp[r][c] = min(dp[r+1][c], dp[r][c+1]) - dungeon[r][c]
        Space can be reduced to 1-D.

        This problem can't be solved by iterating from top-left,
        because the optimal path depends on the future demons.
        '''
        d = dungeon
        R, C = len(d), len(d[0])
        dp = [[float('inf')] * (C + 1) for _ in range(R + 1)]
        dp[R][C - 1] = 1
        dp[R - 1][C] = 1
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                need = min(dp[r + 1][c], dp[r][c + 1]) - d[r][c]
                dp[r][c] = 1 if need <= 0 else need
        return dp[0][0]