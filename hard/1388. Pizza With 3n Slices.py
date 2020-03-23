# 1388. Pizza With 3n Slices
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        '''
        DP.
        We pick elements that are not adjacent, and we pick totally len(slices) // 3 slices.
        
        Similar to 213. House Robber II.
        '''
        A = slices
        # To avoid handling cycle, we move the smallest element to the start of the array.
        idx = A.index(min(A))
        A = A[idx:] + A[0:idx]

        # helper returns the max size if we take 'k' non-adjacent slices from the first 'i' elements.
        @functools.lru_cache(None)
        def helper(k, i):
            if k * 2 - 1 > i:
                return -math.inf
            if k == 1:
                return max(A[:i + 1])
            return max(A[i] + helper(k - 1, i - 2), helper(k, i - 1))
        return helper(len(A) // 3, len(A) - 1)