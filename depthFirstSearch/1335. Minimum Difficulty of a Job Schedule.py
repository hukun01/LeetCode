# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        The key for performance is to compute the current max as we go deeper
        in the search tree.
        '''
        if d > len(jobDifficulty):
            return -1
        cache = {}
        def dfs(idx, d):
            if (idx, d) in cache:
                return cache[(idx, d)]
            if d == 1:
                return max(jobDifficulty[idx:])
            total = float('inf')
            maxDiff = 0
            for i in range(idx, len(jobDifficulty) - d + 1):
                maxDiff = max(maxDiff, jobDifficulty[i])
                total = min(total, maxDiff + dfs(i + 1, d - 1))
            cache[(idx, d)] = total
            return total
        return dfs(0, d)