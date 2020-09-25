# 1590. Make Sum Divisible by P
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        '''
        Two Sum.
        '''
        if (extra := sum(nums) % p) == 0:
            return 0
        seen = {0: -1}
        prefix_sum = 0
        ans = n = len(nums)
        for i, a in enumerate(nums):
            prefix_sum += a
            # looking for (k*p + extra)
            if (need := (prefix_sum - extra) % p) in seen:
                ans = min(ans, i - seen[need])
            prefix_sum %= p
            seen[prefix_sum] = i
        return ans if ans < n else -1