# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        To make the logic clear, do all the boundaries update at the end of
        the while loop.

        Note that when processing the last row and the first column, need to
        check for duplicates.
        '''
        if not matrix or not matrix[0]:
            return []

        ans = []
        row_start, row_end = 0, len(matrix)
        col_start, col_end = 0, len(matrix[0])
        while row_start < row_end and col_start < col_end:
            # top row
            for col in range(col_start, col_end):
                ans.append(matrix[row_start][col])
            # right col
            for row in range(row_start+1, row_end):
                ans.append(matrix[row][col_end-1])
            # bottom row if not overlapped with top row
            if row_start != row_end - 1:
                for col in reversed(range(col_start, col_end-1)):
                    ans.append(matrix[row_end-1][col])
            # left col if not overlapped with right col
            if col_start != col_end - 1:
                for row in reversed(range(row_start+1, row_end-1)):
                    ans.append(matrix[row][col_start])

            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1

        return ans