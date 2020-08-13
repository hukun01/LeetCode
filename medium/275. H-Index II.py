# 275. H-Index II
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        Binary search.
        To count the number of citations that are greater than the
        testing value, leverage the *sorted* citations array.
        '''
        N = len(citations)
        l, h = 0, N - 1
        while l <= h:
            m = (l + h) // 2
            hIdx = N - m
            if citations[m] < hIdx:
                l = m + 1
            else:
                h = m - 1

        return N - l