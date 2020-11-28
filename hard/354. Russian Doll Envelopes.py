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
        [[1, 2], [1, 3]], to ensure the 'w' is increasing, we can sort 'h'
        descending. This way we ensure after picking one 'h' at a 'w', no more
        higher 'h' can be found with the same 'w'.
        '''
        def lis(arr):
            dp = []
            for a in arr:
                i = bisect_left(dp, a)
                if i == len(dp):
                    dp.append(a)
                else:
                    dp[i] = a
            return len(dp)
        return lis([x[1] for x in sorted(envelopes, key=lambda e: (e[0], -e[1]))])