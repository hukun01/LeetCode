# 1749. Maximum Absolute Sum of Any Subarray
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        Prefix sums.
        The subarray sum(nums[i:j]) = presums[j] - presums[i]
        Any subarray sum <= max(presums) - min(presums), so the max subarray
        sum is max(presums) - min(presums).
        The same logic also applies to absolute subarray sum.

        Proof:
        Assume max prefix sum is presums[ma], min prefix sum is presums[mi].
        Two cases to consider:
        1. ma comes after mi, aka, [x,x,x, mi, x,x, ma, x,x].
           The subarray sum in [mi:ma] must be the max one to bring the presum
           from min to max, if there's other bigger subarray sum, the position
           of mi or ma must be different.
        2. ma comes before mi. Same logic as in #1, we just (virtually) reverse
           the array and do the same analysis.

        Note that we need to use initial=0 in case all numbers are positive.

        Time: O(n)
        Space: O(1)
        '''
        find_max, find_min = tee(accumulate(nums, initial=0), 2)
        return max(find_max) - min(find_min)