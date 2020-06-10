# 1458. Max Dot Product of Two Subsequences
class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:
        '''
        1/2 DFS with memoization.
        Similar to LCS problems. One trick here is to not take the subroutine's return value,
        if it's negative. This part is similar to the max subarray sum problem.
        '''
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == -1 or j == -1:
                return -math.inf
            return max(
                A[i] * B[j] + max(0, dfs(i - 1, j - 1)),
                dfs(i, j - 1),
                dfs(i - 1, j))

        return dfs(len(A) - 1, len(B) - 1)

        '''
        2/2 DP.
        Same idea as above, except this just does it from bottom-up.
        '''
        n, m = len(A), len(B)
        dp = [[0] * (m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = A[i] * B[j]
                if i and j: dp[i][j] += max(dp[i - 1][j - 1], 0)
                if i: dp[i][j] = max(dp[i][j], dp[i - 1][j])
                if j: dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]