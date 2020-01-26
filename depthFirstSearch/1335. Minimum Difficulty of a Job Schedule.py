# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        A = jobDifficulty
        n = len(A)
        if n < d:
            return -1
        
        cache = {}
        def dfs(jobId, d):
            if (jobId, d) in cache:
                return cache[(jobId, d)]
            if d == 1:
                return max(A[jobId:])
            res, maxd = float('inf'), 0
            for j in range(jobId, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            cache[(jobId, d)] = res
            return res
    
        return dfs(0, d)