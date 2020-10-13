# 416. Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        DFS with pruning. First, sort the nums with reversed order, so we can do pruning later.
        Second, we can start with the biggest number nums[0], because it must be in either sub-array.
        '''
        if (total := sum(nums)) % 2 == 1:
            return False
        target = total // 2

        @lru_cache(None)
        def dfs(i, curr_sum):
            if i == len(nums):
                return False
            if curr_sum >= target:
                return curr_sum == target
            return dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)
        return dfs(0, 0)
        '''
        Let dp[i][j] denote whether the first i numbers can add up to a sum j.
        
        Then dp[i][j] = dp[i-1][j] if we don't pick the i-th number, or it equals to 
        dp[i-1][j-nums[i]] if we pick the i-th number.
        
        Note that dp[i][j] is determined by dp[i-1], so we can reduce the 2d array into 1d.
        Hence, dp[j] = dp[j] or dp[j-nums[i]]
        Note that we need to reversely traverse the inner loop to ensure that we don't erase
        our own footprints.
        '''
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in reversed(range(num, target+1)):
                dp[j] = dp[j] or dp[j - num]
        return dp[target]