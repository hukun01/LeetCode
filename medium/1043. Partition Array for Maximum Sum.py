# 1043. Partition Array for Maximum Sum
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''
        1/2 DP.
        Let f[i] be the answer for A[:i].
        f[j] = max(f[j], 
                   f[i - 1] + cur_max * (j - i + 1)
                       for j in range(i, min(i + k, n + 1)))
        '''
        n = len(arr)
        f = [0] * (n + 1)
        for i in range(1, n+1):
            cur_max = 0
            for j in range(i, min(i+k, n+1)):
                cur_max = max(cur_max, arr[j-1])
                f[j] = max(f[j], f[i-1] + cur_max * (j - i + 1))

        return f[n]
        '''
        2/2 Memoized DFS.
        '''
        @cache
        def dfs(start):
            ans = 0
            cur_max = 0
            for i in range(start, min(len(A), start + K)):
                cur_max = max(A[i], cur_max)
                ans = max(ans, cur_max * (i - start + 1) + dfs(i + 1))
            return ans
        return dfs(0)