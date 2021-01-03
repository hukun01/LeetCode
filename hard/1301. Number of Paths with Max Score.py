# 1301. Number of Paths with Max Score
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        '''
        DP.
        We are looking for *number* of paths, not the paths themselves,
        so we can use DP.
        Every DP entry is [maxScore, pathCount], and f[r][c] is determined
        by the maxScore and pathCount in its right, bottom and right-bottom neighbors.

        To make it cleaner in iteration, we can go from top left to bottom right.

        One key is to skip paths whose count is 0.

        Time: O(RC)
        Space: O(RC) can be reduced to O(C) as f[r][c] only depends on
        f[r-1][c], f[r][c-1], and f[r-1][c-1].
        '''
        b = board
        R, C = len(b), len(b[0])
        f = [[[0] * 2 for c in range(C)] for r in range(R)]
        f[0][0] = [0, 1]
        MOD = 10 ** 9 + 7
        for r in range(R):
            for c in range(C):
                char = b[r][c]
                if char in 'EX':
                    continue

                if char == 'S':
                    score = 0
                else:
                    score = int(char)

                for dr, dc in ((0, -1), (-1, 0), (-1, -1)):
                    nr, nc = dr + r, dc + c
                    if not 0 <= nr < R or not 0 <= nc < C:
                        continue
                    if f[nr][nc][1] == 0: # can't go down if there is no path
                        continue

                    if f[r][c][0] < f[nr][nc][0]:
                        f[r][c] = f[nr][nc][:]
                    elif f[r][c][0] == f[nr][nc][0]:
                        f[r][c][1] += f[nr][nc][1]
                f[r][c][0] += score
                f[r][c][1] %= MOD
        return f[-1][-1]