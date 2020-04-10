# 1043. Partition Array for Maximum Sum
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        '''
        TODO
        '''
        f = [0] * len(A)
        for i in range(len(A)):
            curMax = A[i]
            for k in range(1, K + 1):
                if i - k + 1 < 0:
                    break
                curMax = max(curMax, A[i - k + 1])
                f[i] = max(f[i], curMax * k)
                if i - k >= 0:
                    f[i] = max(f[i], f[i - k] + curMax * k)
        return f[-1]