# 312. Burst Balloons
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        DP.
        Let f[i][j] be the max coins from bursting balloons between nums[i:j+1],
        f[i][j] = max(f[i][k] + nums[i] * nums[k] * nums[j] + f[k][j])
        '''
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dp(left, right):
            ans = 0
            for i in range(left+1, right):
                ans = max(ans, nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right))
            return ans

        return dp(0, len(nums)-1)