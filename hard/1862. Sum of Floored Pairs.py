# 1862. Sum of Floored Pairs
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        '''
        Prefix frequencies.

        Notice that the value range is within 10 ^ 5, this usually means we
        can generate linear amount of relevant info to help. In this case, we
        need to know how many tuples (a, b) where b >= a.

        A common trap is to do it with division, e.g., a = 3, b1 = 4, b2 = 8,
        the total should be 4//3 + 8//3 = 3. However, in division approach we
        may add up b1 and b2 then do the division, which results in 12//3 = 4.
        This is because we didn't handle remainders properly, but the issue is
        that handlind remainders requires us to check every tuple, which is too
        slow because that needs O(n^2) time.

        Instead of division, we try multiplication. Since the value range is
        small, for every number a from input, we can try a*2, a*3, etc.
        To process the whole input, we need 'n * (1/a + 1/2a + 1/3a)', where
        'a' can be any number, so the worst case we traverse all possible 'a',
        and do 'n * (1/1 + 1/2 + 1/3 + .. + 1/upper_bound)' which is
        'n * H(upper_bound)', and H(upper_bound) is roughly log(upper_bound),
        because H(upper_bound) is a Harmonic Progression.
        Hence, total time is actually O(n log(upper_bound)), or O(n log(n)).

        For each 'a', we need to know all its multiples 'i', and how many do we
        have for each. To answer the second question, we need to count the
        prefix frequency F, then F[i] = F[i + a - 1] - F[i-1]. Note that we
        also need to handle the case where 'i + a - 1' exceeds the range, so
        we do min(upper_bound - 1, i + a - 1). F[i + a - 1] gives us the count
        of all elements >= i but less than the next multiple.

        Note: we need to process every distinct 'a', otherwise, input like
        [1] * 9999 + [1000] would hit TLE.

        Time: O(n log(n))
        Space: O(n)
        '''
        freqs = Counter(nums)
        UB = max(freqs) + 1
        prefix_freqs = list(accumulate(freqs[i] for i in range(UB)))

        ans = 0
        for a, count in freqs.items():
            for i in range(a, UB, a):
                r = i // a
                d = prefix_freqs[min(UB-1, i + a - 1)] - prefix_freqs[i-1]
                ans += r * d * count

        return ans % (10 ** 9 + 7)