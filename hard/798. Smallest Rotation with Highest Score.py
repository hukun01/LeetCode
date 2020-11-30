# 798. Smallest Rotation with Highest Score
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        '''
        Difference array.
        Different rotation k leads to different total score, namely,
        scores[k] = scores[k-1] + diff[k], where diff[k] is the difference
        brought by the k-th rotation.

        As A[i] falls in [0, len(A)], but 0 and len(A) values don't impact
        the total score regardless of k. Every other A[i] has up to two
        intervals of k values, in which it will get one point:
            1. A[i] <= i, intervals are
                a. [0, i - A[i]], A[i] moves left until A[i] reaches i-th.
                b. [i+1, n-1], A[i] wraps around until A[i] reaches (i+1)th.
            2. A[i] > i, interval is [i+1, i - A[i] + n], A[i] wraps around.

        Given the intervals of k for each A[i] that gains one point, our goal
        is to find the most overlapped intervals. It's similar to applying +1
        update to various intervals in the range of [0, len(A)], and find the
        largest update. This is where difference array helps. For more about
        difference array, see 1109. Corporate Flight Bookings.

        Time: O(n)
        Space: O(n)
        '''
        n = len(A)
        diff = [0] * (n + 1)
        for i, a in enumerate(A):
            if a <= i:
                diff[0] += 1
                diff[i - a + 1] -= 1
                diff[i+1] += 1
                diff[n] -= 1
            else:
                diff[i+1] += 1
                diff[i - a + n + 1] -= 1
        score = list(itertools.accumulate(diff))[:-1]
        return score.index(max(score))