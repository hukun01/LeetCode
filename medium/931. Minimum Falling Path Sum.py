# 931. Minimum Falling Path Sum
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        '''
        DP.
        dp[r][c] = A[r][c] + min(dp[r-1][c], dp[r-1][c-1], dp[r-1][c+1]),
        beware of the boundaries.
        If we are not allowed to modify input, we can use 2 1-D arrays.
        '''
        for row in range(1, len(A)):
            for col in range(len(A[0])):
                col1 = max(0, col - 1)
                col2 = min(col + 1, len(A[0]) - 1)
                A[row][col] += min(A[row-1][col], A[row-1][col1], A[row-1][col2])
        return min(A[-1])