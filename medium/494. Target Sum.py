class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        1/2 Subset sum problem.
        Let P be the positive numbers, N be the negative numbers. We have below equations:
                          sum(P) - sum(N) = S
        sum(P) + sum(N) + sum(P) - sum(N) = S + sum(P) + sum(N)
                               2 * sum(P) = S + sum(nums)
                                   sum(P) = (S + total) // 2
        The problem now is asking us to find the number of positive number subsets
        whose sum is a target.

        Let f[i][j] be the number of ways to achieve a sum j in the first i numbers.
        f[i][j] = f[i-1][j] + f[i-1][j-num].
        Since f[i] only depends on f[i-1], we can reduce the space to 1D.
        '''
        total = sum(nums)
        if (S + total) % 2 == 1 or total < S:
            return 0
        target = (S + total) // 2
        f = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        f[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(target + 1):
                f[i][j] = f[i-1][j]
                if j - nums[i-1] >= 0:
                    f[i][j] += f[i-1][j - nums[i-1]]
        return f[-1][-1]
        '''
        2/2 DFS with memoization
        '''
        @functools.lru_cache(None)
        def dfs(idx, currSum):
            if idx == len(nums):
                if currSum == S:
                    return 1
                return 0
            return dfs(idx + 1, currSum + nums[idx]) + dfs(idx + 1, currSum - nums[idx])
        return dfs(0, 0)