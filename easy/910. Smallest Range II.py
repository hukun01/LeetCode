# 910. Smallest Range II
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        '''
        Sort.
        Note that the ans would never be greater than 'max(A) - min(A)', as
        we can always add K to all A elelement, to make no diff change.

        Based on this, we can try to reduce the diff. Intuitively, we want to
        increase the smaller half of A, and decrease the larger half of A.
        Look for the point whose left elements are increased, and right parts
        are decreased. Try each possible point in the array, increase its left,
        and decrease its right, and track the current (max - min).

        In part1 (increasing), the min is 'A[0] + K', max is 'A[i] + K'.
        In part2 (decreasing), the max is 'A[-1] - K', min is 'A[i+1] - K'.

        For each point we try, the max element among two parts is the max
        between part1's max and part2's max, aka, max(A[i] + K, part2_max).
        Similarly, the min element among two parts is the min between part1's
        min and part2's min, aka, min(A[i+1] - K, part1_min).

        Time: O(n log(n)) where n is len(A)
        Space: O(n) from sort
        '''
        A.sort()
        ans = A[-1] - A[0]
        part1_min = A[0] + K
        part2_max = A[-1] - K
        for i in range(len(A) - 1):
            max_i = max(A[i] + K, part2_max)
            min_i = min(A[i+1] - K, part1_min)
            ans = min(ans, max_i - min_i)
        return ans