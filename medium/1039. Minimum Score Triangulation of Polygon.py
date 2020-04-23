# 1039. Minimum Score Triangulation of Polygon
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        '''
        1/2 DFS with memoization.
        '''
        @functools.lru_cache(None)
        def dfs(i, j):
            if i + 1 >= j:
                return 0
            res = math.inf
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + A[i] * A[k] * A[j] + dfs(k, j))
            return res
        return dfs(0, len(A) - 1)
        '''
        2/2 DP bottom up
        Let f[i][j] be the answer for A[i:j]
        f[i][j] = f[i][k] + f[k][j] + min(A[i] * A[k] * A[j] for k in [i+1, j))
        Final anser is f[0][end].
        Note that, since we build big chunks of f[i][j] based on small ones,
        we need to enumerate all i~j intervals from smallest size to largest.
        '''
        n = len(A)
        f = [[0] * n for _ in range(n)]
        for d in range(2, n):
            for i in range(n - d):
                j = i + d
                f[i][j] = min(f[i][k] + f[k][j] + A[i]*A[k]*A[j] for k in range(i + 1, j))
                    
        return f[0][n-1]