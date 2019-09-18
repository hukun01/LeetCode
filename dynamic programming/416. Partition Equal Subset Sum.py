class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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