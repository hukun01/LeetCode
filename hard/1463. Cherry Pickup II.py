# 1463. Cherry Pickup II
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        The key is to only add a cell once if the two robots overlap,
        but otherwise it's a straightforward DFS with cache.
        '''
        R, C = len(grid), len(grid[0])
        @functools.lru_cache(None)
        def dfs(row, c1, c2):
            if row == R:
                return 0
            if not 0 <= c1 < C or not 0 <= c2 < C:
                return 0
            r = grid[row]
            if c1 != c2:
                ans = r[c1] + r[c2]
            else:
                ans = r[c1]
            
            nextMax = 0
            for n1 in range(c1 - 1, c1 + 2):
                for n2 in range(c2 - 1, c2 + 2):
                    nextMax = max(nextMax, dfs(row + 1, n1, n2))
            return ans + nextMax
        return dfs(0, 0, len(grid[0]) - 1)