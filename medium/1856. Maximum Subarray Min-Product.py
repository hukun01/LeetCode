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
        maxArea = 0
        for i, h in enumerate(nums + [0]):
            start = i
            while left and h <= left[-1][0]:
                prevH, prevStart = left.pop()
                maxArea = max(maxArea, (prefix_sums[i] - prefix_sums[prevStart]) * prevH)
                start = prevStart
            left.append((h, start))

        return maxArea % (10 ** 9 + 7)