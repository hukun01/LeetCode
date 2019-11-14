class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Similar to House Robber, in this problem we exclude the first house, and run the
        first solution; and exclude the last house, and run the first solution, and pick the bigger one.
        '''
        if len(nums) <= 2:
            return max(nums + [0])
        
        def rob1(nums):
            if len(nums) <= 2:
                return max(nums + [0])
            dp = [0] * len(nums)
            dp[0] = nums[0]
            for i in range(1, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        return max(rob1(nums[:-1]), rob1(nums[1:]))