# 1301. Number of Paths with Max Score
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        '''
        We are looking for *number* of paths, not the paths themselves,
        so we can use DP.
        Every DP entry is [maxScore, pathCount], and dp[r][c] is determined
        by the maxScore and pathCount in its right, bottom and right-bottom neighbors.
        '''
        N = len(board)
        # tuple is [score, pathCount]
        dp = [[[0, 0] for c in range(N + 1)] for r in range(N + 1)]
        dp[N - 1][N - 1] = [0, 1]
        for r in reversed(range(N)):
            for c in reversed(range(N)):
                if board[r][c] in 'XS':
                    continue
                for dr, dc in [[0, 1], [1, 0], [1, 1]]:
                    lastTuple = dp[r + dr][c + dc]
                    score = dp[r][c][0]
                    if score < lastTuple[0]:
                        dp[r][c] = lastTuple[:]
                    elif score == lastTuple[0]:
                        dp[r][c][1] += lastTuple[1]
                if board[r][c] != 'E':
                    dp[r][c][0] += int(board[r][c])
        if dp[0][0][1] == 0:
            return [0, 0]
        dp[0][0][1] %= 10 ** 9 + 7
        return dp[0][0]