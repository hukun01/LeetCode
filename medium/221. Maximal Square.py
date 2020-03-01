# 221. Maximal Square
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        '''
        A square is defined by its bottom right corner.
        A maximum square is defined by the shortest edge next
        to the bottom right corner. Only when the top square and 
        the left square and the top left square have the same edge,
        the new bigger square can be formed.
        Note that we can use 2 rows instead of len(matrix)+1 rows.
        '''
        if not matrix or not matrix[0]:
            return 0
        ans = 0
        rows, cols = len(matrix), len(matrix[0])
        # solution 1/2
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1
                    ans = max(ans, dp[r][c])
        return ans ** 2

        '''
        solution 2/2
        Note that in above code we only use the current row and the last row,
        so we can use 2 rows instead of len(matrix)+1 rows. Just need to reset the
        current row to 0 when the cell is not "1".

        dp = [[0] * (cols+1) for _ in range(2)]
        for r in range(1, rows+1):
            currRow = (r-1) % 2
            lastRow = 1 - currRow
            for c in range(1, cols+1):
                if matrix[r-1][c-1] == "1":
                    dp[currRow][c] = min(dp[currRow][c-1], dp[lastRow][c], dp[lastRow][c-1]) + 1
                    ans = max(ans, dp[currRow][c])
                else:
                    dp[currRow][c] = 0
        return ans ** 2
        '''