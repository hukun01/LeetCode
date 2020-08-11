# 312. Burst Balloons
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        1/2 Memoized DFS.
        Memoization seems unintuitive at first glance, because after bursting
        the first nums[i], its adjacent elements are affected, thus the future
        score is affected. This issue makes the problem impossible for DP.
        
        Now, think reversely, would the score be affected if bursting the
        *last* nums[i]? No. If we know we are going to burst nums[i] as the
        last balloon in (left, right) exclusively, the balloons are separated
        into 2 parts, left part is (left, i), right part is (i, right).
        We can try each possible i in (left, right), and handle left and
        right parts accordingly.

        Let f[i][j] be the max coins from bursting balloons between (i, j)
        exclusively,
        f[i][j] = max(f[i][k] + nums[i] * nums[k] * nums[j] + f[k][j])
        '''
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):
            ans = 0
            for i in range(left+1, right):
                ans = max(ans, nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right))
            return ans

        return dp(0, len(nums)-1)
        '''
        2/2 DP.
        Since f[i][j] depends on f[i][k] and f[k][j], both of which are
        smaller intervals, we can enumerate all the possible interval lengths,
        and calculate f[i][j] on smaller intervals. Then f[i][j] on bigger
        intervals can be built on smaller intervals.
        '''
        nums = [1] + nums + [1]
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for i in range(left + 1, right):
                    f[left][right] = max(
                        f[left][right],
                        nums[left] * nums[i] * nums[right] + f[left][i] + f[i][right])
        return f[0][n - 1]