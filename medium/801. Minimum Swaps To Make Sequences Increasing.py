# 801. Minimum Swaps To Make Sequences Increasing
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        '''
        DP.
        Let f[i][0] be the answer for the A[:i] and B[:i] if we don't swap i-th,
        Let f[i][1] be the answer for the A[:i] and B[:i] if we swap i-th.
        See state transition in code.

        Time: O(n)
        Space: O(n) can be optimized to O(1).
        '''
        n = len(A)
        f = [[inf, inf] for _ in range(n)]
        f[0] = [0, 1]
        for i in range(1, n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                f[i][0] = f[i-1][0]
                # if we swap i-th, we should swap (i-1)th as well
                f[i][1] = f[i-1][1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                f[i][0] = min(f[i][0], f[i-1][1])
                # if we didn't swap at (i-1)th, we need to swap at i-th.
                f[i][1] = min(f[i][1], f[i-1][0] + 1)

        return min(f[-1])