# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        '''
        Prefix sum + greedy.
        Whenever we see a good interval and it's not overlapped with the
        last one, we can take it.
        '''
        last_idx = -1
        ans = cur = 0
        seen = {0:-1}
        for i, n in enumerate(nums):
            cur += n
            if (dif := cur - target) in seen and seen[dif] >= last_idx:
                ans += 1
                last_idx = i
            seen[cur] = i
        return ans