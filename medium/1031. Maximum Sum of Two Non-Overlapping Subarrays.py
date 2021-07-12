# 1031. Maximum Sum of Two Non-Overlapping Subarrays
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        '''
        Iterate array twice.
        Use Lsum to denote the sum of subarray with at most L numbers, Lmax to
        denote the max Lsum we have seen so far. Use Msum and Mmax similarly.

        In the first iteration, we keep L at left, M at right, so we keep
        adding to Msum, and keep sliding the M window and poping out the left
        side of M. In the meantime, when we exceed M numbers, we can start
        adding those to Lsum, and keep poping out the left side of L once we
        exceed L + M. We keep updating the Lmax, and Lmax + Msum is a candidate
        for the answer.
        The key is to only add to the right part, and ensure it has M element,
        before exploring the left part and finding its max sum. This is to find
        the max left sum, while trying all possible right sums. We can't do the
        opposite to try all left sums with the max right sum, because the right
        sum can be in the middle, and overlap with some of the left sums.

        In the second iteration, the logic is similar, but we keep M at left,
        L at right.

        Time: O(n) where n is len(A)
        Space: O(1)
        '''
        ans = Lsum = Lmax = Msum = 0
        for i, a in enumerate(A):
            Msum += a
            if i - M >= 0:
                Msum -= A[i - M]
                Lsum += A[i - M]
            if i - L - M >= 0:
                Lsum -= A[i - L - M]
            Lmax = max(Lmax, Lsum)
            ans = max(ans, Msum + Lmax)

        Lsum = Msum = Mmax = 0
        for i, a in enumerate(A):
            Lsum += a
            if i - L >= 0:
                Lsum -= A[i - L]
                Msum += A[i - L]
            if i - L - M >= 0:
                Msum -= A[i - L - M]
            Mmax = max(Mmax, Msum)
            ans = max(ans, Lsum + Mmax)

        return ans