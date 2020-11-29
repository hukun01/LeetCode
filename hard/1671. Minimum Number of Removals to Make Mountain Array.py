# 1671. Minimum Number of Removals to Make Mountain Array
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        '''
        1/2 DP.
        At each index i, we find the length of LIS from left side to i, and
        length of LIS from the 'reversed' right side to i. Note that we let
        nums[i] to be the largest element in both LIS. If both LIS a and b
        has at least 2 elements, then the mountain is (a + b - 1), and the
        removal count is the remaining.

        Time: O(n^2 log(n)) where n is the length of nums. This is based on the
        O(n) for loop and LIS sub-procedure O(nlog(n)).
        Space: O(n).
        '''
        def LIS(arr):
            dp = [math.inf] * len(arr)
            for a in arr:
                dp[bisect_left(dp, a)] = a
            return bisect_left(dp, math.inf)
        ans = 0
        n = len(nums)
        for i in range(1, n - 1):
            left = [x for x in nums[:i] if x < nums[i]] + [nums[i]]
            right = [nums[i]] + [x for x in nums[i+1:] if x < nums[i]]
            right = right[::-1]
            a = LIS(left)
            b = LIS(right)
            if a >= 2 and b >= 2:
                ans = max(ans, a + b - 1)
        return n - ans
        '''
        2/2 DP optimized.
        Based on 1/2, we don't need to re-calculate LIS at every index, we can
        just calculate them once for nums, and do it again but reservely.
        During this process we record lens where lens[i] is the length of LIS
        ending at nums[i].
        Note that we reverse the output of LIS from reversed nums, just for
        easier processing.

        Time: O(nlog(n))
        Space: O(n)
        '''
        def LIS(arr):
            dp = [math.inf] * len(arr)
            lens = [0] * len(arr)
            for i, a in enumerate(arr):
                pos = bisect_left(dp, a)
                lens[i] = pos + 1
                dp[pos] = a
            return lens
        l1 = LIS(nums)
        l2 = LIS(nums[::-1])[::-1]
        ans = 0
        n = len(nums)
        for a, b in zip(l1, l2):
            if a >= 2 and b >= 2:
                ans = max(ans, a + b - 1)
        return n - ans