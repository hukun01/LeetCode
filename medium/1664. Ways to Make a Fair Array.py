# 1664. Ways to Make a Fair Array
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        '''
        1/2 Prefix sums.
        Calculate the prefix sums for even-index and odd-index nums.
        At each index i:
            new even sum = even_sums[:i] + odd_sums[i+1:]
            new odd sum  = odd_sums[:i] + even_sums[i+1:]
        Add one if new even sum == new odd sum.

        Time: O(N) where N is the length of the nums array.
        Space: O(N).
        '''
        n = len(nums)
        odds = [0] * (n + 1)
        evens = [0] * (n + 1)
        for i, a in enumerate(nums):
            if i % 2 == 0:
                evens[i + 1] = evens[i] + a
                odds[i + 1] = odds[i]
            else:
                evens[i+1] = evens[i]
                odds[i + 1] = odds[i] + a
        ans = 0
        for i in range(n):
            new_even_sum = evens[i] + odds[-1] - odds[i+1]
            new_odd_sum = odds[i] + evens[-1] - evens[i+1]
            ans += new_even_sum == new_odd_sum
        return ans
        '''
        2/2 Prefix diff sums.
        Calculate the (even - odd) prefix sums.
        At each index i: new diffs = diffs[:i] - diffs[i+1:]
        [(even - odd) before i] + [(odd(new even) - even(new odd)) after i]
        Add one if new diffs becomes 0.

        Time and space complexities are the same as 1/2, but this approach is
        cleaner as there's less confusion on index.
        '''
        n = len(nums)
        diffs = [0] * (n + 1)
        for i in range(n):
            if i % 2 == 0:
                diffs[i+1] = diffs[i] + nums[i]
            else:
                diffs[i+1] = diffs[i] - nums[i]
        ans = 0
        for i in range(n):
            diff_before_i = diffs[i]
            diff_after_i = -(diffs[n] - diffs[i + 1])
            ans += (diff_before_i + diff_after_i == 0)
        return ans
    