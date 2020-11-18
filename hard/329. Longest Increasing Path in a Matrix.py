# 329. Longest Increasing Path in a Matrix
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        DFS with memoization.
        Normally DFS/BFS would require a visited set to avoid going back to
        the same nodes, but in this scenario we don't need such set, because
        we only go to the bigger numbers. Based on this, we can also cache
        the result from each position, as two longest paths (a, b) and (c, d)
        can be merged if b < c.

        Time: O(RC) where R is the number of rows, C is the number of columns.
        Space: O(RC) for the cache.
        '''
        if not matrix or not matrix[0]:
            return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):
            ans = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if matrix[nr][nc] <= matrix[r][c]:
                    continue
                ans = max(ans, 1 + dfs(nr, nc))
            return ans
        ans = 0
        for r in range(R):
            for c in range(C):
                ans = max(ans, 1 + dfs(r, c))
        return ans