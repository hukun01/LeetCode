class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Similar to House Robber, in this problem we run the same solution when
        1. excluding the first house;
        2. excluding the last house.
        And pick the bigger result.
        '''
        if len(nums) <= 2:
            return max(nums + [0])
        
        def rob1(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        return max(rob1(nums[:-1]), rob1(nums[1:]))