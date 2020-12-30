# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        '''
        Prefix sum + greedy.
        Whenever we see a good interval and it's not overlapped with the last
        one, we can take it.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        last_idx = -1
        ans = cur_sum = 0
        seen = {0:-1}
        for i, a in enumerate(nums):
            cur_sum += a
            if (diff := cur_sum - target) in seen and seen[diff] >= last_idx:
                ans += 1
                last_idx = i
            seen[cur_sum] = i
        return ans