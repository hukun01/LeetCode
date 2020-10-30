# 799. Champagne Tower
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        '''
        DP.
        The key is to keep track of total amount of through traffic, instead
        of adding traffic incrementally.
        Start from the top, for each cell at a row, if it has excess traffic,
        distribute the excess equally to its next row, and cap it at 1.
        As the current row only impacts the next one, this solution's space
        complexity can be reduced to 1-D.
        '''
        A = [[0] * k for k in range(1, 102)]
        A[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                if (amount := A[r][c]) >= 1:
                    extra = (amount - 1) / 2
                    A[r+1][c] += extra
                    A[r+1][c+1] += extra
                    A[r][c] = 1

        return A[query_row][query_glass]