# 775. Global and Local Inversions
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        '''
        Notice that local inversions is a subset of global inversions, so
        we just need to see if there is any non-local gobal inversion.

        The original order should be [0, 1, ...i, i + 1, ..., N - 1].
        Local inversions are swaps between two adjacent elements only.
        So whenever we find |i - A[i]| > 1, it's a non-local global inversion.

        Time: O(n) where n is len(A)
        Space: O(1)
        '''
        return all(abs(i - a) <= 1 for i, a in enumerate(A))