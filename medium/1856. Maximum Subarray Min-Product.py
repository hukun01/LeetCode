# 1856. Maximum Subarray Min-Product
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        '''
        Mono stack.

        Same as 84. Largest Rectangle in Histogram, just change the histogram
        width with sum.

        Time: O(n)
        Space: O(n)
        '''
        prefix_sums = list(accumulate([0] + nums + [0]))
        left = []
        ans = 0
        for i, h in enumerate(nums + [0]):
            start = i
            while left and left[-1][0] > h:
                prev_h, prev_start = left.pop()
                ans = max(ans, (prefix_sums[i] - prefix_sums[prev_start]) * prev_h)
                start = prev_start
            left.append((h, start))

        return ans % (10 ** 9 + 7)