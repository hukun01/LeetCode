# 576. Out of Boundary Paths
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        '''
        Memoized DFS
        '''
        MOD = 10 ** 9 + 7
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        @lru_cache(None)
        def find(r, c, times):
            if not (0 <= r < m and 0 <= c < n):
                return 1
            if times == 0:
                return 0
            ans = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                ans += find(nr, nc, times - 1)
            return ans % MOD
        return find(i, j, N)