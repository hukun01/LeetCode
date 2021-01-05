# 1712. Ways to Split Array Into Three Subarrays
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        '''
        1/2 Binary search + prefix sums.
        Focus on the mid part, let 'left' be its left boundary, for every 'left',
        find its range of 'right', such that sum[:left] <= sum[left:right] <= sum[right:],
        aka, presums[left] <= presums[right] - presums[left] <= presums[-1] - presums[right],
        while 'left' is in [1, n-2].
        Above equation can be transformed to
        2*presums[left] <= presums[right] <= (presums[-1] + presums[left]) // 2.
        Hence, we can find the min and max 'right' using binary search.

        Note that the 'right_lb' is the inclusive index that satisfies the
        above equation, while 'right_ub' is the exclusive index where
        'right_ub - 1' satisfies the above equation.

        Time: O(n log(n)) where n is len(nums)
        Space: O(n)
        '''
        MOD = 10 ** 9 + 7
        presums = list(accumulate([0] + nums))

        n = len(nums)
        ans = 0
        for left in range(1, n-1):
            right_lb = bisect_left(presums, 2 * presums[left])
            right_ub = bisect_left(presums, (presums[left] + presums[-1]) // 2 + 1)
            ans += max(0, min(n, right_ub) - max(left + 1, right_lb))
            ans %= MOD

        return ans
        '''
        2/2 Three pointers + prefix sums.
        Based on the equation from 1/2, we have
        2*presums[left] <= presums[right] <= (presums[-1] + presums[left]) // 2
        Then we have
        2*presums[left] <= presums[right_lb] <= presums[right_ub], and
        2*presums[right_lb] <= 2*presums[right_ub] <= presums[-1] + presums[left]

        As sum[:left] only increases, we know sum[left:right_lb] must also
        increase, so right_lb only moves right. Same as right_ub.
        As right_lb and right_ub only increase, we can track them outside of
        the for loop where we identify them for each 'left'.

        Note that the 'right_lb' is the inclusive index that satisfies the
        above equation, while 'right_ub' is the exclusive index where
        'right_ub - 1' satisfies the above equation. Hence, the 2 inner while
        loops are actually quite different, although they look similar.

        Time: O(n)
        Space: O(n)
        '''
        MOD = 10 ** 9 + 7
        presums = list(accumulate([0] + nums))

        n = len(nums)
        ans = 0
        right_lb = right_ub = 0
        for left in range(1, n-1):
            right_lb = max(right_lb, left + 1)
            while right_lb < n and presums[right_lb] < 2 * presums[left]:
                right_lb += 1
            right_ub = max(right_ub, right_lb)
            while right_ub < n and 2 * presums[right_ub] <= presums[-1] + presums[left]:
                right_ub += 1
            ans += right_ub - right_lb
            ans %= MOD

        return ans