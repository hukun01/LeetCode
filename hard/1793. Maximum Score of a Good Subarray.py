# 1793. Maximum Score of a Good Subarray
class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        '''
        Greedy.
        We have to include k in the middle, so we start from k and expand to
        left and right.
        Then there's one decision to make, go to left, or right? The answer is
        to go to the side with greater value, because that impacts less to our
        result which depends on the min value we see so far.

        Time: O(n) where n is len(A)
        Space: O(1)
        '''
        res = mini = A[k]
        i, j, n = k, k, len(A)
        while i > 0 or j < n - 1:
            if (A[i - 1] if i else 0) < (A[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            mini = min(mini, A[i], A[j])
            res = max(res, mini * (j - i + 1))
        return res