# 1568. Minimum Number of Days to Disconnect Island
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        '''
        DFS + brainteaser.
        Note that there can be up to 2 days, because any corner can be cut
        in 2 days.
        If there's one island at the beginning, we just try every cell, if
        the cur works, return 1, otherwise return 2.
        '''
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        def mark(r, c, visited):
            def dfs(r, c):
                if (r, c) in visited or grid[r][c] != 1:
                    return
                visited.add((r, c))
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if not 0 <= nr < R or not 0 <= nc < C:
                        continue
                    dfs(nr, nc)
            dfs(r, c)
        def count():
            used = set()
            ans = 0
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 1 and (r, c) not in used:
                        mark(r, c, used)
                        ans += 1
            return ans
        if count() != 1:
            return 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    continue
                grid[r][c] = 0
                if count() != 1:
                    return 1
                grid[r][c] = 1
        return 2