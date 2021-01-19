# 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        '''
        Prefix sum + 2sum + greedy.
        Use prefix sums to quickly determine if the needed interval sum exists.
        We are looking for interval [i, j] such that [:j] - [:i] = target.
        Use prefix sum to track [:j], use 'seen' to track previous prefix sums,
        our goal is to find 'cur_sum - target'.
        Whenever we find one, we can reset the 'seen', as we can't use any
        previous prefix sums from now.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        ans = cur_sum = 0
        seen = set([0])
        for a in nums:
            cur_sum += a
            if (cur_sum - target) in seen:
                seen = set()
                ans += 1
            seen.add(cur_sum)
        return ans