# 354. Russian Doll Envelopes
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        Longest increasing subsequence.

        The first thought is to sort the envelopes by their (w, h), and find
        the length of LIS from it. But the issue is that there can be data
        like [[1, 2], [3, 1]], so the 2nd dimension isn't really sorted.
        Given that the 1st dimension is sorted, we can find the length of LIS
        in the 2nd dimension, but when we have the same 'w' like
        [[1, 2], [1, 3]], we would choose both elements, but 'w' is not
        increasing. We only pick one 'h' from the same 'w', so we  sort 'h'
        by descending. This way we ensure after picking one 'h' at a 'w', no
        more higher 'h' can be found with the same 'w', thus no duplicate 'w'.

        The key is to reduce a 2d problem to 1d with the first dimension of
        problem be solved separately.

        Time: O(n log(n)) where n is len(envelopes)
        Space: O(n)
        '''
        def LIS(arr):
            n = len(arr)
            ans = [inf] * (n + 1)
            for a in arr:
                ans[bisect_left(ans, a)] = a
            return bisect_left(ans, inf)

        envelopes.sort(key=lambda e: (e[0], -e[1]))
        return LIS([e[1] for e in envelopes])