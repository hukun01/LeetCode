# 1691. Maximum Height by Stacking Cuboids
class Solution:
    def maxHeight(self, A: List[List[int]]) -> int:
        '''
        DP.
        Let f[i] be the answer for A[:i+1], then we have
        f[i] = max(f[j] + h[i] for all j where A[j] <= A[i]).
        As cuboids can be stacked only if all 3 dimensions are in order, we
        sort each cuboid and the whole array, and use the largest dimension as
        height for each cuboid.
        Now this is similar to LIS, 300. Longest Increasing Subsequence.

        Time: O(n^2)
        Space: O(n)
        '''
        for c in A:
            c.sort()
        A.sort()
        n = len(A)
        f = [0] * n
        for i in range(n):
            for j in range(i):
                # A[i][0] is ensured by sorting
                if A[i][1] >= A[j][1] and A[i][2] >= A[j][2]:
                    f[i] = max(f[i], f[j])
            f[i] += A[i][2]
        return max(f)