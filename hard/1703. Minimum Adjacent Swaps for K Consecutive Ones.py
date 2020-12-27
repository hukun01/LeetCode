# 1703. Minimum Adjacent Swaps for K Consecutive Ones
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        '''
        Transform + sliding window median.
        Assume the positions of ones are p_i to p_(i+k-1), we need to find
        k positions, q + 0, q + 1, ..., q + k - 1, to hold the ones. The min
        moves would be to move all ones to the median of the k positions,
        which is ∑_i=0_(k-1) (|p_i - q + i|).
        Let g(i) = p_i - i, we transform the above equation to
        ∑_i=0_(k-1) (|g(i) - q|).
        The above equation is the smallest when q is median of the g(i)s in
        scope. We can pre-compute all g(i), so now the problem is to try all
        possible k-window g(i)s and record the min, which can be solved by a
        sliding window of size k recording the median of g(i)s.
        The equation would be
        ∑_j=i_(i+k-1) (|g(j) - q|)
        = ∑_j=i_(mid_idx-1) (q - g(j)) + ∑_j=(mid_idx+1)_(i+k-1) (g(j) - q)
        = (mid_idx - i) * q - ∑_j=i_(mid_idx-1) (g(j))
          - (i + k - 1 - mid_idx) * q + ∑_j=(mid_idx+1)_(i+k-1) (g(j))
        = (2*mid_idx - 2*i - k + 1) * q + ∑_j=(mid_idx+1)_(i+k-1) (g(j)) - ∑_j=i_(mid_idx-1) (g(j))
        = (2*mid_idx - 2*i - k + 1) * q + range_sum1 - range_sum2

        In the current sliding window has g(i), ..., g(i+k-1), mid_idx = (2i + k - 1) // 2.
        And the two range_sums can be pre-computed using prefix sums in O(1) time.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        p = [i for i, a in enumerate(nums) if a == 1]
        g = [p_i - i for i, p_i in enumerate(p)]
        # g_pre_sums[i] is the prefix sum of g[:i], g[i] is excluded.
        g_pre_sums = list(accumulate([0] + g))

        def g_range_sum(start, end):
            return g_pre_sums[end+1] - g_pre_sums[start]

        ans = inf
        for i in range(len(g) - k + 1):
            mid_idx = (2 * i + k - 1) // 2
            q = g[mid_idx]
            range_sum1 = g_range_sum(mid_idx + 1, i + k - 1)
            range_sum2 = g_range_sum(i, mid_idx - 1)
            result = (2*mid_idx - 2 * i - k + 1) * q + range_sum1 - range_sum2
            ans = min(ans, result)
        return ans