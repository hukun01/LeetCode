# 980. Unique Paths III
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        '''
        Backtracking.
        '''
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(grid), len(grid[0])
        total = 0
        start = None
        for r in range(R):
            for c in range(C):
                total += (grid[r][c] != -1)
                if grid[r][c] == 1:
                    start = (r, c)
        def dfs(visited, r, c):
            if grid[r][c] == 2:
                if len(visited) == total:
                    return 1
                return 0
            ans = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                if (nr, nc) in visited:
                    continue
                if grid[nr][nc] not in (0, 2):
                    continue
                visited.add((nr, nc))
                ans += dfs(visited, nr, nc)
                visited.remove((nr, nc))
            return ans

        return dfs({start}, *start)