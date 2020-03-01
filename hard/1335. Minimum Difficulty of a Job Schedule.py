# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        1/2 DP with monotic stacks. Much faster than 2nd solution.
        '''
        A = jobDifficulty
        n = len(A)
        if n < d: return -1
        
        dp, dp2 = [float('inf')] * n, [0] * n
        for d in range(d):
            stack = []
            for i in range(d, n):
                dp2[i] = dp[i - 1] + A[i] if i else A[i]
                while stack and A[stack[-1]] <= A[i]:
                    j = stack.pop()
                    dp2[i] = min(dp2[i], dp2[j] - A[j] + A[i])
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