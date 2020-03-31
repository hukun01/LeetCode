# 1301. Number of Paths with Max Score
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        '''
        We are looking for *number* of paths, not the paths themselves,
        so we can use DP.
        Every DP entry is [maxScore, pathCount], and dp[r][c] is determined
        by the maxScore and pathCount in its right, bottom and right-bottom neighbors.
        
        To make it cleaner in iteration, we can go from top left to bottom right.

        One key is to 
        '''
        b = board
        R, C = len(b), len(b[0])
        dp = [[[0] * 2 for c in range(C)] for r in range(R)]
        dp[0][0] = [0, 1]
        for r in range(R):
            for c in range(C):
                char = b[r][c]
                if char in 'EX':
                    continue
                elif char == 'S':
                    score, count = 0, 0
                else:
                    score, count = int(char), 1
                for dr, dc in ((0, -1), (-1, 0), (-1, -1)):
                    nr, nc = dr + r, dc + c
                    if not 0 <= nr < R or not 0 <= nc < C:
                        continue
                    if dp[nr][nc][1] == 0: # can't go down if there is no path
                        continue
                    if dp[nr][nc][0] + score > dp[r][c][0]:
                        dp[r][c] = [dp[nr][nc][0] + score, dp[nr][nc][1]]
                    elif dp[nr][nc][0] + score == dp[r][c][0]:
                        dp[r][c][1] += dp[nr][nc][1]
        MOD = 10 ** 9 + 7
        return [dp[-1][-1][0], dp[-1][-1][1] % MOD]