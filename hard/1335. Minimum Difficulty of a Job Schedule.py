# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        1/2 DP with monotic stacks. Much faster than the 2nd solution.
        '''
        j = jobDifficulty
        n = len(j)
        if n < d: return -1
        
        dp, dp2 = [float('inf')] * n, [0] * n
        for day in range(d):
            stack = []
            for i in range(day, n):
                dp2[i] = dp[i - 1] + j[i] if i else j[i]
                while stack and j[stack[-1]] <= j[i]:
                    idx = stack.pop()
                    dp2[i] = min(dp2[i], dp2[idx] - j[idx] + j[i])
                if stack:
                    dp2[i] = min(dp2[i], dp2[stack[-1]])
                stack.append(i)
            dp, dp2 = dp2, [0] * n
        return dp[-1]
        '''
        2/2 DFS
        The key for performance is to compute the current max as we go deeper
        in the search tree.
        '''
        j = jobDifficulty
        n = len(j)
        if d > n:
            return -1
        cache = {}
        def dfs(idx, d):
            if (idx, d) in cache:
                return cache[(idx, d)]
            if d == 1:
                return max(j[idx:])
            total = float('inf')
            maxJob = 0
            for i in range(idx, n - d + 1):
                maxJob = max(maxJob, j[i])
                total = min(total, maxJob + dfs(i + 1, d - 1))
            cache[(idx, d)] = total
            return total
        return dfs(0, d)