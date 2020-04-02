# 1335. Minimum Difficulty of a Job Schedule
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        '''
        1/2 DP with monotonic decreasing stacks. Much faster than the 2nd solution.
        
        Let dp[i][j] be the min difficulty with the first i days and j jobs.
        Transitions:
        dp[i][j] = max(dp[i-1][j-1] + jobs[j], dp[i][x] - jobs[x] + job[j]),
        first option is to take the j-th job and finish the i-th day;
        second option is to take the max(jobs[x:j+1]) at i-th day, where x is the last
        job that's smaller than jobs[j].

        The monotonic decreasing stack is used to find the last smaller job, and help
        skip all the intermediate jobs that are bigger, which can't be a better schedule.
        '''
        jobs = jobDifficulty
        n = len(jobs)
        if n < d: return -1
        
        dp, dp2 = [float('inf')] * n, [0] * n
        for day in range(d):
            stack = []
            for i in range(day, n):
                dp2[i] = dp[i - 1] + jobs[i] if i else jobs[i]
                while stack and jobs[stack[-1]] <= jobs[i]:
                    idx = stack.pop()
                    dp2[i] = min(dp2[i], dp2[idx] - jobs[idx] + jobs[i])
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
        jobs = jobDifficulty
        n = len(jobs)
        if d > n:
            return -1
        cache = {}
        def dfs(idx, d):
            if (idx, d) in cache:
                return cache[(idx, d)]
            if d == 1:
                return max(jobs[idx:])
            total = float('inf')
            maxJob = 0
            for i in range(idx, n - d + 1):
                maxJob = max(maxJob, jobs[i])
                total = min(total, maxJob + dfs(i + 1, d - 1))
            cache[(idx, d)] = total
            return total
        return dfs(0, d)