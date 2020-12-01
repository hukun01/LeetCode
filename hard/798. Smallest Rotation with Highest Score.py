# 798. Smallest Rotation with Highest Score
class Solution:
    def bestRotation(self, A: List[int]) -> int:
        '''
        Difference array.
        Different rotation k leads to different total score, namely,
        let scores[k] be the total score with rotation k.

        Every A[i] has up to two intervals of k, in which it will get 1 point:
            1. A[i] <= i, intervals are
                a. [0, i - A[i]], A[i] moves left until A[i] reaches i-th.
                b. [i+1, n-1], A[i] wraps around until A[i] reaches (i+1)th.
            2. A[i] > i, interval is [i+1, i - A[i] + n], A[i] wraps around.

        Given the intervals of k for each A[i] that gains one point, our goal
        is to find the most overlapped intervals. It's similar to applying +1
        update to various intervals in the range of [0, len(A)], each interval
        is updated up to n times. Then find the largest updated point after all
        updates are done. However, updating scores for every A[i] means O(n^2)
        time, too slow. This is where difference array helps. For more about
        difference array, see 1109. Corporate Flight Bookings.
        Let scores[k] = scores[k-1] + diff[k], where diff[k] is the difference
        brought by updating from (k-1) to k rotations. We store the updates in
        diff in O(1) time, and get the final result once by accumulating diff,
        with O(n) time.

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
        score = list(accumulate(diff))[:-1]
        return score.index(max(score))