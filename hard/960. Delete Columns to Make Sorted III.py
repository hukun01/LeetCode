# 960. Delete Columns to Make Sorted III
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        '''
        LIS.
        Treat each whole column as one element in a 1d array. Then we can
        transform the problem into finding the LIS where each column is one
        element. The answer is n - LIS.

        Time: O(n m^2) where n is len(A[0]), m is len(A).
        Space: O(n)
        '''
        n = len(A[0])
        f = [1] * n
        for i in range(1, n):
            for j in range(i):
                if all(row[j] <= row[i] for row in A):
                    f[i] = max(f[i], f[j] + 1)

        return n - max(f)