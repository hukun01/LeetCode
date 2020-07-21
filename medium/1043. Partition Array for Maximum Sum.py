# 1043. Partition Array for Maximum Sum
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''
        1/2 DP.
        Let f[i] be the answer for A[:i].
        f[i] = 0
        f[i] = max(f[i - k] + curr_max * k for k in [1, min(i, K))
        '''
        f = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            curr_max = A[i - 1]
            for k in range(1, min(i, K) + 1):
                curr_max = max(curr_max, A[i - k])
                f[i] = max(f[i], f[i - k] + curr_max * k)
        return f[-1]
        '''
        2/2 Memoized DFS.
        '''
        @lru_cache(None)
        def dfs(start):
            ans = 0
            curr_max = 0
            for i in range(start, min(len(A), start + K)):
                curr_max = max(A[i], curr_max)
                ans = max(ans, curr_max * (i - start + 1) + dfs(i + 1))
            return ans
        return dfs(0)