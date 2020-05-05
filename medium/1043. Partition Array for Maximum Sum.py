# 1043. Partition Array for Maximum Sum
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''
        DP.
        Let f[i] be the answer for A[:i].
        f[i] = 0
        f[i] = max(f[i - k] + curMax * k for k in [1, min(i, K))
        '''
        f = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            curMax = A[i - 1]
            for k in range(1, min(i, K) + 1):
                curMax = max(curMax, A[i - k])
                f[i] = max(f[i], f[i - k] + curMax * k)
        return f[-1]