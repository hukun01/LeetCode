# 221. Maximal Square
class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        '''
        DP.

        A square is defined by its bottom right corner.
        A maximum square is defined by the shortest edge next
        to the bottom right corner. Only when the top square and 
        the left square and the top left square have the same edge,
        the new bigger square can be formed.
        Note that we can use 2 rows instead of len(M)+1 rows.

        Time: O(R C)
        Space: O(R C) can be reduced to O(C)
        '''
        R, C = len(M), len(M[0])
        f = [[0] * (C + 1) for _ in range(R + 1)]
        max_edge = 0
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if M[r-1][c-1] == '0':
                    continue

                f[r][c] = min(f[r-1][c], f[r][c-1], f[r-1][c-1]) + 1
                max_edge = max(max_edge, f[r][c])

        return max_edge ** 2