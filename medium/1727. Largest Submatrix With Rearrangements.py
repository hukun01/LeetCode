# 1727. Largest Submatrix With Rearrangements
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        '''
        Sort + greedy.
        Every row can be the base for the max submatrix. Hence we try each row
        as the base row. We look for consecutive ones on each column, and sort
        the current row, reversely. As we iterate through the current row, we
        can greedily take the current column (number of consecutive ones) as
        the shortest edge for matrix, and record its area.

        Time: O(R C log(C)) for row sorting inside row iteration.
        Space: O(C) to create sorted single row
        '''
        R, C = len(matrix), len(matrix[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                if matrix[r][c] > 0 and r - 1 >= 0:
                    matrix[r][c] += matrix[r-1][c]
            
            sorted_row = sorted(matrix[r], reverse=True)
            for i in range(C):
                ans = max(ans, sorted_row[i] * (i + 1))

        return ans