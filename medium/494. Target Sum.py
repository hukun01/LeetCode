class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        1/3 Translate into subset sum problem. Then DP.
        Let P be the positive numbers, N be the negative numbers. We have below equations:
                          sum(P) - sum(N) = S
        sum(P) + sum(N) + sum(P) - sum(N) = S + sum(P) + sum(N)
                               2 * sum(P) = S + sum(nums)
                                   sum(P) = (S + total) // 2
        The problem now becomes 416. Partition Equal Subset Sum.

        Let f[i][j] be the number of ways to achieve a sum j in the first i numbers.
        f[i][j] = f[i-1][j] + f[i-1][j-num].
        
        Since f[i] only depends on f[i-1], we can reduce the space to 1D.
        Note that when using a rolling 1D array, we need to reverse the inner loop,
        because we don't want to erase our own footprint in the last row when updating
        the current row. 
        Alternatively, we can use a new row, and swap it with current row after each inner loop.
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
        2/3 Optimized space based on 1/3 DP.
        '''
        total = sum(nums)
        if (S + total) % 2 == 1 or total < S:
            return 0
        target = (S + total) // 2
        f = [0] * (target + 1)
        f[0] = 1
        for n in nums:
            for j in range(target, n-1, -1):
                f[j] += f[j - n]
        return f[-1]
        '''
        3/3 DFS with memoization.
        '''
        @functools.lru_cache(None)
        def dfs(idx, currSum):
            if idx == len(nums):
                if currSum == S:
                    return 1
                return 0
            return dfs(idx + 1, currSum + nums[idx]) + dfs(idx + 1, currSum - nums[idx])
        return dfs(0, 0)